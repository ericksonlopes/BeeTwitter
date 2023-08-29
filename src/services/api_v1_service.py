from tweepy import User

from config.auth_tweepy import get_twitter_conn_v1


class APITwitterV1Service:

    @classmethod
    def __api(cls):
        return get_twitter_conn_v1()

    def get_user(self, screen_name: str) -> User:
        return self.__api().get_user(screen_name=screen_name)
