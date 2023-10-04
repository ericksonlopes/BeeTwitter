from datetime import datetime

import openai
from loguru import logger

from bee_twitter.config.settings import API_KEY_OPENAI
from bee_twitter.helpers.auth_tweepy import get_twitter_conn_v2


class TrendAnalyzer:
    api_key = API_KEY_OPENAI

    def __init__(self):
        self.today = datetime.today().strftime('%d-%m-%Y')

    @staticmethod
    def get_tweets(trend) -> str:
        try:
            api = get_twitter_conn_v2()

            data = api.search_recent_tweets(query=f'{trend} lang:pt -is:retweet', max_results=10)

            str_tweets = ''

            for trend in data[0]:
                trend_trans = trend.text
                trend_trans = trend_trans.replace('\n', '')
                trend_trans = trend_trans.replace('#', '')
                trend_trans = trend_trans.strip()

                str_tweets += trend_trans

            logger.info(f"Tweets coletados com sucesso para {trend}: {str_tweets}")

            return str_tweets
        except Exception as error:
            logger.error(f"Erro ao coletar tweets: {error}")

    def analyze_trend(self, trend) -> str:
        openai.api_key = self.api_key

        tweets = self.get_tweets(trend)

        prompt = f"""
        Gere um resumo baseado na trend a seguir: {trend}.

        Tome como base os seguintes tweets: {tweets}

        Use a data de hoje como referencia ({self.today})

        Extras:
        Remove os links dos tweets.
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=750,
            n=7,
            stop=None,
            temperature=0.4,
            frequency_penalty=0.2,
            presence_penalty=0.0
        )

        text = response['choices'][0]['text']

        logger.info(f"Resumo gerado com sucesso para {trend}: {text}")

        return text
