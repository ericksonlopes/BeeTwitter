from tweepy import Response

from bee_twitter.helpers.auth_tweepy import get_twitter_conn_v2
from loguru import logger

class APITwitterV2Service:
    @classmethod
    def client(cls):
        return get_twitter_conn_v2()

    def get_tweets(self, _id: str, max_results: int = 5) -> Response:
        try:
            return self.client().get_users_tweets(id=_id, max_results=max_results, tweet_fields=[
                'created_at',
                'public_metrics',
                'text',
                'id',
                'entities',
                'author_id',
                "attachments",
                "context_annotations",
                "conversation_id",
                "edit_controls",
                "edit_history_tweet_ids",
                "geo",
                "in_reply_to_user_id",
                "lang",
                "note_tweet",
                "possibly_sensitive,"
                "referenced_tweets",
                "reply_settings",
                "source",
                "withheld",
            ])

        except Exception as e:
            logger.error(f'Error on get tweets: {e}')


if __name__ == '__main__':
    api = APITwitterV2Service()
    print(api.get_tweets(_id='2244994945'))
