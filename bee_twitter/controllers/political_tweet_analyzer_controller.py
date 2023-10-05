import re

from loguru import logger

from bee_twitter.config.settings import API_KEY_OPENAI
from bee_twitter.openai_analyzer.political_tweet_analyzer import PoliticalTweetAnalyzer
from bee_twitter.repository.connect_cosmos import CosmosDBManager
from bee_twitter.repository.connect_snowflake import ConnectorSnowflake
from bee_twitter.repository.models.cosmos import AppAuthorQuality
from bee_twitter.repository.models.snowflake import TweetModel
from bee_twitter.repository.models.snowflake.tweet_model_analysis import TweetQualityModel


class PoliticalTweetAnalyzerController:
    api_key = API_KEY_OPENAI

    @staticmethod
    def insert_tweet_analyzed_in_cosmos(categories: list[tuple[str, str]], tweet: TweetModel, texto: str):

        categories_dict = [
            {"order": index, "name": category[0], "quality_value": category[1]}
            for index, category in enumerate(categories)
        ]

        quality_value = float(
            [category["quality_value"] for category in categories_dict if category["name"] == 'geral'][0]
        )

        author_quality = AppAuthorQuality(
            id=str(tweet.id_tweet),
            cod_status=1,
            id_publisher=7,
            id_author=tweet.author_id,
            quality_result=texto,
            quality_value=quality_value,
            quality_results=categories_dict
        )

        # Adicione o objeto ao contêiner usando o CosmosDBManager
        db_manager = CosmosDBManager(container_name="app_author_quality")
        db_manager.add_object(author_quality)

    def analyze_tweet(self, session, tweet):
        try:
            political_tweet = PoliticalTweetAnalyzer(self.api_key)

            return_analyze = political_tweet.analyze_tweet(tweet.text)
        except Exception as e:
            logger.error(f'Erro ao analisar tweet: {tweet.id} - {e}')
            return e

        categories = re.findall(r'(\w+):\s(\d+)%', return_analyze)

        if categories is None:
            logger.warning(f'Tweet não analisado corretamente: {tweet.id}, tentando novamente.')
            self.analyze_tweet(session, tweet)

        texto = re.search(r'texto:\s(.+)', return_analyze).group(1)

        for category in categories:
            tweet_quality = TweetQualityModel(
                id_tweet=tweet.id_tweet,
                text=texto,
                tweet_text=tweet.text,
                dt_creation=tweet.created_at,
                dt_update=tweet.created_at,
                dt_expiration=tweet.created_at,
                url=tweet.url,
                author_id=tweet.author_id,
                quality_results_name=category[0],
                quality_results_value=category[1],
            )
            session.add(tweet_quality)

        try:
            self.insert_tweet_analyzed_in_cosmos(categories, tweet, texto)
        except Exception as e:
            logger.error(f'Erro ao salvar tweet no Cosmos: {tweet.id} - {e}')
            raise e

    def run(self):
        with ConnectorSnowflake() as session:
            tweet_to_process = session.query(TweetModel).filter(TweetModel.ind_analysis == False).all()

            list_id_tweets = [tweet.id_tweet for tweet in tweet_to_process]

            if len(list_id_tweets) == 0:
                logger.info('Nenhum tweet para analisar')
                return

        for tweet_id in list_id_tweets:

            with ConnectorSnowflake() as session:
                try:
                    tweet = session.query(TweetModel).filter(TweetModel.id_tweet == tweet_id).first()

                    if tweet is None:
                        logger.warning(f'Tweet não encontrado: {tweet_id}')
                        continue

                    self.analyze_tweet(session, tweet)

                    tweet.ind_analysis = True

                    logger.info(f'Tweet analisado e atualizado: {tweet.id}')
                except Exception as e:
                    logger.error(f'Erro ao analisar tweet: {tweet_id} - {e}')
                    session.rollback()
