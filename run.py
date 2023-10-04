from bee_twitter.controllers.get_tweets_by_author import GetTweetsByAuthor
from bee_twitter.controllers.political_tweet_analyzer_controller import PoliticalTweetAnalyzerController
from bee_twitter.controllers.trend_analyzer_controller import TrendAnalyserControl


def get_tweets():
    api = GetTweetsByAuthor()
    api.get_tweets_user(screen_name='jairbolsonaro')


def analyze_tweets():
    pta = PoliticalTweetAnalyzerController()
    pta.run()


def get_trends():
    trend = TrendAnalyserControl()
    trend.run()


if __name__ == '__main__':
    # get_tweets()
    # analyze_tweets()
    get_trends()
