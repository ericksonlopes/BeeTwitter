import re

from loguru import logger

from bee_twitter.repository.connect import Connector
from bee_twitter.repository.models import *
from bee_twitter.services import APITwitterV1Service
from bee_twitter.services.api_twitter_services.api_v2_service import APITwitterV2Service


class GetTweetsByAuthor(APITwitterV2Service, APITwitterV1Service):
    def __init__(self):
        super().__init__()

    def get_tweets_user(self, screen_name: str):
        logger.info(f"Iniciando coleta de tweets para o usuário: {screen_name}")

        try:
            id_author = self.get_user_id(screen_name=screen_name)

            tweets = self.get_tweets(_id=id_author)
            data = tweets.data

            meta = tweets.meta

            if tweets.errors:
                logger.info(f"Erros: {tweets.errors.__dict__}")

            for tweet in data:
                try:
                    texto = tweet.get('text', None)

                    with Connector() as session:
                        exists = session.query(TweetModel).filter(TweetModel.id_tweet == tweet.get('id', None)).first()

                        if exists:
                            logger.info(f"Tweet já existe: {tweet.get('id', None)}")
                            continue

                    url = re.findall(r'\bhttps?://\S+\b', texto)

                    if len(url) > 0:
                        url = url[-1]
                    else:
                        url = None

                    with Connector() as session:
                        exists = session.query(TweetModel).filter(TweetModel.id == tweet.get('id', None)).first()

                        if exists:
                            continue

                    tweet_model_add = TweetModel(
                        ind_analysis=False,
                        id_tweet=tweet.get('id', None),
                        text=texto,
                        created_at=tweet.get('created_at', None),
                        url=url,
                        retweet_count=tweet.get('public_metrics', {}).get('retweet_count', None),
                        reply_count=tweet.get('public_metrics', {}).get('reply_count', None),
                        like_count=tweet.get('public_metrics', {}).get('like_count', None),
                        quote_count=tweet.get('public_metrics', {}).get('quote_count', None),
                        bookmark_count=tweet.get('public_metrics', {}).get('bookmark_count', None),
                        impression_count=tweet.get('public_metrics', {}).get('impression_count', None),

                        author_id=tweet.get('author_id', None),
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

                    )

                    with Connector() as session:
                        session.add(tweet_model_add)

                    logger.info(f"Tweet adicionado com sucesso: {tweet.get('id', None)}")
                    logger.info(f"Buscand mais informações sobre o tweet: {tweet.get('id', None)}")
                except Exception as error:
                    logger.error(f"Erro ao criar o objeto TweetModel: {error}")

                    continue

                # context annotations
                try:
                    if tweet.get('context_annotations', None) is None:
                        continue

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
                    logger.error(f"context_annotations {error}")

                # entities annotations
                try:
                    if tweet.get("entities", {}).get("annotations", None) is None:
                        continue

                    for annotation in tweet["entities"]["annotations"]:
                        entities_annotations = EntitiesAnnotationsModel(
                            tweet_id=tweet.get('id', None),
                            start=annotation.get("start", None),
                            end=annotation.get("end", None),
                            probability=annotation.get("probability", None),
                            type=annotation.get("type", None),
                            normalized_text=annotation.get("normalized_text", None)
                        )

                        with Connector() as session:
                            session.add(entities_annotations)

                except Exception as error:
                    logger.error(f"entities.annotations: {error}")

                # entities cashtags
                try:
                    if tweet.get("entities", {}).get("cashtags", None) is None:
                        continue

                    for cashtag in tweet["entities"]["cashtags"]:
                        cashtag_model = EntitiesCashtagsModel(
                            tweet_id=tweet.get('id', None),
                            start=cashtag.get("start", None),
                            end=cashtag.get("end", None),
                            tag=cashtag.get("tag", None)
                        )

                        with Connector() as session:
                            session.add(cashtag_model)

                except Exception as error:
                    logger.error(f"entities.cashtags {error}")

                # entities hashtags
                try:
                    if tweet.get("entities", {}).get("hashtags", None) is None:
                        continue

                    for hashtag in tweet["entities"]["hashtags"]:
                        hashtag_model = EntitiesHashtagsModel(
                            tweet_id=tweet.get('id', None),
                            start=hashtag.get("start", None),
                            end=hashtag.get("end", None),
                            tag=hashtag.get("tag", None)
                        )

                        with Connector() as session:
                            session.add(hashtag_model)

                except Exception as error:
                    logger.error(f"entities.hashtags {error}")

                # entities mentions
                try:
                    if tweet["entities"]["mentions"] is None:
                        continue

                    for mention in tweet["entities"]["mentions"]:
                        mention_model = EntitiesMentionsModel(
                            tweet_id=tweet.get('id', None),
                            start=mention.get("start", None),
                            end=mention.get("end", None),
                            tag=mention.get("tag", None)
                        )

                        with Connector() as session:
                            session.add(mention_model)

                except Exception as error:
                    logger.error(f"entities.mentions {error}")

                # entities urls
                try:
                    if tweet.get("entities", {}).get("urls", None) is None:
                        continue

                    for url in tweet["entities"]["urls"]:
                        url_model = EntitiesUrlsModel(
                            tweet_id=tweet.get('id', None),
                            start=url.get("start", None),
                            end=url.get("end", None),
                            url=url.get("url", None),
                            expanded_url=url.get("expanded_url", None),
                            display_url=url.get("display_url", None),
                            status=url.get("status", None),
                            title=url.get("title", None),
                            description=url.get("description", None),
                            unwound_url=url.get("unwound_url", None)
                        )

                        with Connector() as session:
                            session.add(url_model)

                except Exception as error:
                    logger.error(f"entities.urls {error}")

                # referenced_tweets
                try:
                    if tweet.get("referenced_tweets", None) is None:
                        continue

                    for referenced_tweet in tweet["referenced_tweets"]:
                        referenced_model = ReferencedTweetsModel(
                            tweet_id=tweet.get('id', None),
                            type=referenced_tweet.get("type", None),
                            id_Referenced=referenced_tweet.get("id", None)
                        )

                        with Connector() as session:
                            session.add(referenced_model)

                except Exception as error:
                    logger.error(f"referenced_tweets {error}")

                # attachments poll
                try:
                    if tweet.get("attachments", {}).get("poll_ids", None) is None:
                        continue

                    for poll in tweet["attachments"]["poll_ids"]:
                        poll_model = AttachmentsPoll(
                            tweet_id=poll.get('id', None),
                            poll_id=poll
                        )

                        with Connector() as session:
                            session.add(poll_model)

                except Exception as error:
                    logger.error(f"attachments.poll_ids {error}")

                # attachments midea_keys
                try:
                    if tweet.get("attachments", {}).get("midea_keys", None) is None:
                        continue

                    for midea_key in tweet["attachments"]["midea_keys"]:
                        midea_key_model = AttachmentsMedia(
                            tweet_id=tweet.get('id', None),
                            midea_key=midea_key
                        )

                        with Connector() as session:
                            session.add(midea_key_model)

                except Exception as error:
                    logger.error(f"attachments.midea_keys {error}")

        except Exception as error:
            logger.error(f"Erro ao criar o objeto TweetModel: {error}")

        logger.info(f"Coleta de tweets finalizada para o usuário: {screen_name}")
