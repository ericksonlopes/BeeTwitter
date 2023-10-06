import re

from loguru import logger

from bee_twitter.repository.connect_snowflake import ConnectorSnowflake
from bee_twitter.repository.models.snowflake import *
from bee_twitter.services import APITwitterV1Service
from bee_twitter.services.api_twitter_services.api_v2_service import APITwitterV2Service


class GetTweetsByAuthor(APITwitterV2Service, APITwitterV1Service):
    def __init__(self):
        super().__init__()

    def get_author_quality(self, screen_name: str):
        logger.info(f"Iniciando coleta de tweets para o usuário: {screen_name}")

        try:
            id_author = self.get_user_id(screen_name=screen_name)

            tweets = self.get_tweets(_id=id_author)
            data = tweets.data

            meta = tweets.meta

            if tweets.errors:
                logger.info(f"Erros: {tweets.errors.__dict__}")

            for tweet in data:
                try:
                    texto = tweet.get('text', None)

                    with ConnectorSnowflake() as session:
                        exists = session.query(TweetModel).filter(TweetModel.id_tweet == tweet.get('id', None)).first()

                        if exists:
                            logger.info(f"Tweet já existe: {tweet.get('id', None)}")
                            continue

                    url = re.findall(r'\bhttps?://\S+\b', texto)

                    if len(url) > 0:
                        url = url[-1]
                    else:
                        url = None

                    tweet_model_add = TweetModel(
                        ind_analysis=False,
                        id_tweet=tweet.get('id', None),
                        text=texto,
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

                        # Meta
                        result_count=meta.get('result_count', None),
                        newest_id=meta.get('newest_id', None),
                        oldest_id=meta.get('oldest_id', None),
                        next_token=meta.get('next_token', None),

                    )

                    with ConnectorSnowflake() as session:
                        session.add(tweet_model_add)

                    logger.info(f"Tweet adicionado com sucesso: {tweet.get('id', None)}")
                    logger.info(f"Buscand mais informações sobre o tweet: {tweet.get('id', None)}")
                except Exception as error:
                    logger.error(f"Erro ao criar o objeto TweetModel: {error}")
                    continue

        except Exception as error:
            logger.error(f"Erro ao criar o objeto TweetModel: {error}")

        logger.info(f"Coleta de tweets finalizada para o usuário: {screen_name}")
