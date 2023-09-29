import tweepy

from bee_twitter.config.settings import consumer_key, consumer_secret, access_token, access_token_secret, bearer_token


def get_twitter_conn_v1() -> tweepy.API:
    """Get twitter conn 1.1"""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def get_twitter_conn_v2() -> tweepy.Client:
    """Get twitter conn 2.0"""

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        bearer_token=bearer_token
    )

    return client
