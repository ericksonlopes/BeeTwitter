import re

import pandas as pd
from loguru import logger

from bee_twitter.repository.connect_cosmos import CosmosDBManager
from bee_twitter.repository.connect_snowflake import ConnectorSnowflake
from bee_twitter.repository.models.cosmos import AppAuthorQuality
from bee_twitter.repository.models.snowflake import TweetModel, UserModel
from bee_twitter.services import APITwitterV1Service
from bee_twitter.services.api_twitter_services.api_v2_service import APITwitterV2Service
from bee_twitter.services.political_tweet_analyzer import PoliticalTweetAnalyzer


class AuthorTwitterQuality(APITwitterV2Service, APITwitterV1Service):
    def __init__(self, twitter_profile):
        self.twitter_profile = twitter_profile
        self.tweets = []

    @staticmethod
    def save_tweet(tweet, meta, session):
        try:
            url = re.findall(r'\bhttps?://\S+\b', tweet.get('text', None))

            if len(url) > 0:
                url = url[-1]
            else:
                url = None

            tweet_model_add = TweetModel(
                id_tweet=tweet.get('id', None),
                text=tweet.get('text', None),
                created_at=tweet.get('created_at', None),
                url=url,
                retweet_count=tweet.get('public_metrics', {}).get('retweet_count', None),
                reply_count=tweet.get('public_metrics', {}).get('reply_count', None),
                like_count=tweet.get('public_metrics', {}).get('like_count', None),
                quote_count=tweet.get('public_metrics', {}).get('quote_count', None),
                bookmark_count=tweet.get('public_metrics', {}).get('bookmark_count', None),
                impression_count=tweet.get('public_metrics', {}).get('impression_count', None),

                author_id=tweet.get('author_id', None),
                conversation_id=tweet.get('conversation_id', None),
                edits_remaining=tweet.get('edits_remaining', None),

                is_edit_eligible=tweet.get("edit_controls", {}).get("is_edit_eligible", None),
                editable_until=tweet.get("edit_controls", {}).get("editable_until", None),
                edit_history_tweet_ids=str(tweet.get("edit_history_tweet_ids")),
                geo=str(tweet.get("geo", None)),
                in_reply_to_user_id=tweet.get("in_reply_to_user_id", None),
                lang=tweet.get("lang", None),
                possibly_sensitive=tweet.get("possibly_sensitive", None),
                promoted_metrics=str(tweet.get("promoted_metrics", None)),
                reply_settings=tweet.get("reply_settings", None),
                source=tweet.get("source", None),
                withheld=str(tweet.get("withheld", None)),

                result_count=meta.get('result_count', None),
                newest_id=meta.get('newest_id', None),
                oldest_id=meta.get('oldest_id', None),
                next_token=meta.get('next_token', None),
            )

            session.add(tweet_model_add)

        except Exception as e:
            logger.error(f'Error on save tweets: {e}')
            raise e

    def analyze_content_tweet(self, session, tweet, count=0) -> list[dict]:
        try:
            political_tweet = PoliticalTweetAnalyzer()
            return_analyze = political_tweet.analyze_tweet(tweet.text)

        except Exception as e:
            logger.error(f'Erro ao analisar tweet: {tweet.id} - {e}')
            raise e

        categories = re.findall(r'(\w+):\s(\d+)%', return_analyze)

        if categories is None:
            logger.warning(f'Tweet não analisado corretamente: {tweet.id}, tentando novamente.')

            if count == 3:
                logger.warning(f'Tweet não analisado corretamente: {tweet.id}, tentando novamente.')
                raise Exception(f'Tweet não analisado corretamente: {tweet.id}!')

            self.analyze_content_tweet(session, tweet, count)

        categories = re.search(r'texto:\s(.+)', return_analyze).group(1)

        list_categories = []

        for category in categories:
            quality_results_name = category[0]
            quality_results_value = category[1]

            list_categories.append({
                "tweet_id": tweet.id_tweet,
                "quality_results_name": quality_results_name,
                "quality_results_value": quality_results_value
            })

        return list_categories

    @staticmethod
    def save_author_quality_in_cosmos(list_categories, tweet: TweetModel, id_author, session):
        df = pd.DataFrame(list_categories)
        df.groupby('quality_results_name')['quality_results_value'].mean().reset_index()
        dict_categories = df.to_dict('records')

        dict_categories_without_geral = []
        geral_value = 0

        # Use um loop para percorrer cada dicionário na lista
        for dicionario in dict_categories:
            # Verifique se o nome no dicionário é diferente do nome a ser removido
            if "geral" not in dicionario['quality_results_name'].lower():
                # Se for diferente, adicione o dicionário à nova lista
                dict_categories_without_geral.append(dicionario)
            else:
                geral_value = dicionario['quality_results_value']

        author = session.query(UserModel).filter(UserModel.id == id_author).first()

        author_quality = AppAuthorQuality(
            id=str(tweet.get('id', None)),
            author_description=author.description,
            twitter_profile=author.screen_name,
            name=author.name,
            cod_status=1,
            id_publisher=7,
            id_author=author.id,
            quality_result="gerar",
            quality_value=geral_value,
            quality_results=dict_categories_without_geral
        )

        db_manager = CosmosDBManager(container_name="app_author_quality")
        db_manager.add_object(author_quality)

        logger.info(f"Qualidade do autor {author.screen_name} salva com sucesso no cosmos!")

    def get_tweets_by_author(self):
        try:
            id_author = self.get_user_id(screen_name=self.twitter_profile)

            tweets = self.get_tweets(_id=id_author)

            # list_categories = [{
            #     "tweet_id": "123456789",
            #     "quality_results_name": "geral",
            #     "quality_results_value": 0.5
            # },
            #     {
            #         "tweet_id": "123456789",
            #         "quality_results_name": "economia",
            #         "quality_results_value": 0.5
            #     },
            #     {
            #         "tweet_id": "123456789",
            #         "quality_results_name": "educacao",
            #         "quality_results_value": 0.5
            #     },
            # ]

            list_categories = []

            for tweet in tweets.data:
                with ConnectorSnowflake() as session:
                    exists = session.query(TweetModel).filter(TweetModel.id_tweet == tweet.get('id', None)).first()

                    if exists:
                        logger.info(f"Tweet já existe: {tweet.get('id', None)}")
                    else:
                        self.save_tweet(tweet, tweets.meta, session)

                    categories = self.analyze_content_tweet(session, tweet)

                    list_categories.append(*categories)

            self.save_author_quality_in_cosmos(list_categories, tweets.data[0], id_author, session)

        except Exception as e:
            logger.error(f'Error on get tweets by author: {e}')
            raise e


if __name__ == '__main__':
    AuthorTwitterQuality(twitter_profile="jairbolsonaro").get_tweets_by_author()
