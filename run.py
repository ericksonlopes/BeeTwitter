from bee_twitter.controllers.get_tweets_by_author import GetTweetsByAuthor
from bee_twitter.controllers.political_tweet_analyzer_controller import PoliticalTweetAnalyzerController


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
