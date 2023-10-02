from bee_twitter.config.settings import API_KEY_OPENAI
from bee_twitter.controllers.api_v2_controller import TwitterAPIV2
from bee_twitter.controllers.political_tweet_analyzer import PoliticalTweetAnalyzerController


def get_tweets():
    api = TwitterAPIV2()
    api.user(_id='jairbolsonaro')


def analyze_tweets():
    api_key = API_KEY_OPENAI
    pta = PoliticalTweetAnalyzerController(api_key)
    pta.run()


if __name__ == '__main__':
    get_tweets()
    analyze_tweets()
