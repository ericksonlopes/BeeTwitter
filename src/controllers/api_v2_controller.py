from src.repository.connect import Connector
from src.repository.models import TweetModel, ContextAnnotationsDomainModel, ContextAnnotationsEntityModel
from src.services.api_v2_service import APITwitterV2Service


class TwitterAPIV2(APITwitterV2Service):
    def __init__(self):
        super().__init__()

    def user(self, _id: str) -> bool:
        try:
            tweets = self.get_tweets('2670726740')
            data = tweets.data

            meta = tweets.meta

            # todo adicionar os includes
            includes = tweets.includes

            # todo salvar erros no log
            # errors = tweets.__dict__["errors"]

            for tweet in data:
                try:
                    tweet_model = TweetModel(
                        id=tweet.get('id', None),
                        text=tweet.get('text', None),
                        created_at=tweet.get('created_at', None),
                        retweet_count=tweet.get('public_metrics', {}).get('retweet_count', None),
                        reply_count=tweet.get('public_metrics', {}).get('reply_count', None),
                        like_count=tweet.get('public_metrics', {}).get('like_count', None),
                        quote_count=tweet.get('public_metrics', {}).get('quote_count', None),
                        bookmark_count=tweet.get('public_metrics', {}).get('bookmark_count', None),
                        impression_count=tweet.get('public_metrics', {}).get('impression_count', None),
                        referenced_tweets=tweet.get('referenced_tweets', None),
                        entites=str(tweet.get('entities', None)),
                        author_id=tweet.get('author_id', None),
                        attachments=str(tweet.get('attachments', None)),
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

                        # Includes
                        includes=str(includes.get('includes', None))
                    )

                    with Connector() as session:
                        session.add(tweet_model)

                except Exception as error:
                    print(error, "Erro ao criar o objeto TweetModel")
                    continue

                try:
                    for context_annotations in tweet['context_annotations']:
                        domain = context_annotations['domain']
                        domain_model = ContextAnnotationsDomainModel(
                            tweet_id=tweet.get('id', None),
                            id_domain=domain.get('id', None),
                            name=domain.get('name', None),
                            description=domain.get('description', None)
                        )

                        entity = context_annotations['entity']
                        entity_model = ContextAnnotationsEntityModel(
                            tweet_id=tweet.get('id', None),
                            id_entity=entity.get('id', None),
                            name=entity.get('name', None),
                            description=entity.get('description', None)
                        )

                        with Connector() as session:
                            session.add(domain_model)
                            session.add(entity_model)

                except Exception as error:
                    print(error, "Erro ao criar a sessão")
                    continue

        except Exception as error:
            print(error)
            return False

        return True


if __name__ == '__main__':
    api = TwitterAPIV2()
    api.user(_id='jairbolsonaro')
