import requests
import urllib3
from bs4 import BeautifulSoup
from loguru import logger

from bee_twitter.openai_analyzer.trend_analyzer import TrendAnalyzer
from bee_twitter.repository.connect import Connector
from bee_twitter.repository.models.trends_model import TrendModel


class TrendAnalyserControl:
    URL = "https://trends24.in/brazil/"

    def get_trends(self) -> list[str]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        req = requests.get(self.URL, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5, verify=False)

        req.raise_for_status()

        soup = BeautifulSoup(req.text, "html.parser")

        list_li = soup.find("ol", {"class": "trend-card__list"}).find_all("li")

        list_trends = [trend.a.text.replace("#", "") for trend in list_li]

        logger.info(f"Trends coletados com sucesso: {list_trends}")

        return list_trends

    def run(self):
        list_trends = self.get_trends()

        for trend in list_trends:
            try:
                summary = TrendAnalyzer().analyze_trend(trend)

                trend_model = TrendModel(
                    hashtag=trend,
                    analyzed_tweets=summary
                )

                with Connector() as session:
                    session.add(trend_model)

                logger.info(f"Trend analisada e salva: {trend}")

            except Exception as error:
                logger.error(f"Erro ao analisar trend: {error}")

            break
