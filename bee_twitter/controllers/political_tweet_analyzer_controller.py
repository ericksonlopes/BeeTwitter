import re

from loguru import logger

from bee_twitter.config.settings import API_KEY_OPENAI
from bee_twitter.openai_analyzer.political_tweet_analyzer import PoliticalTweetAnalyzer
from bee_twitter.repository.connect import Connector
from bee_twitter.repository.models import TweetModel
from bee_twitter.repository.models.tweet_model_analysis import TweetQualityModel


class PoliticalTweetAnalyzerController:
    api_key = API_KEY_OPENAI

    @staticmethod
    def tweet_to_dict(tweet) -> dict:

        tweet_dict = {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "url": tweet.url,
            "author_id": tweet.author_id,
        }

        return tweet_dict

    def analyze_tweet(self, session, tweet):
        political_tweet = PoliticalTweetAnalyzer(self.api_key)
        return_analyze = political_tweet.analyze_tweet(tweet.text)

        categories = re.findall(r'(\w+):\s(\d+)%', return_analyze)

        if categories is None:
            logger.info(f'Tweet não analisado: {tweet.id} - {return_analyze}, tentando novamente')
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
            logger.info(f'Tweet analisado e salvo: {tweet.id} - {tweet_quality}')

    def run(self):
        with Connector() as session:
            tweet_to_process = session.query(TweetModel).filter(TweetModel.ind_analysis == False).all()

            list_id_tweets = [tweet.id_tweet for tweet in tweet_to_process]

            if len(list_id_tweets) == 0:
                logger.info('Nenhum tweet para analisar')
                return

        for tweet_id in list_id_tweets:

            with Connector() as session:
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

