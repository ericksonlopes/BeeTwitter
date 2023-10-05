import tweepy
from sqlalchemy import distinct, func

from bee_twitter.config.settings import bearer_token, access_token, access_token_secret
from bee_twitter.repository.connect_snowflake import ConnectorSnowflake
from bee_twitter.repository.models import *

client = tweepy.Client(bearer_token=bearer_token, consumer_key="ODQxT0gzY0JPSjJCTVl5ODAzdHI6MTpjaQ",
                       consumer_secret="Qoo7tqEZbYz0Du6wtgep1jORzEmu-3SNFHub9Ei-XbS1Szrpas",
                       access_token=access_token, access_token_secret=access_token_secret)

# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# api_twitter_services = tweepy.API(auth)

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# api_twitter_services = tweepy.API(auth)


_id = '2670726740'


def get_tweets():
    tweets = client.get_users_tweets(id=_id, max_results=5, tweet_fields=[
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
    ]
                                     )

    # print(tweets)
    print("*" * 100)
    print(tweets.data)
    print(tweets.includes)
    print(tweets.meta)


    # print(".text): ", tweets[0][1].text)
    # print(".id): ", tweets[0][1].id)
    # print(".created_at): ", tweets[0][1].created_at)
    # print(".public_metrics): ", tweets[0][1].public_metrics)
    #
    # print(".entities): ", tweets[0][1].entities)
    # print(".author_id): ", tweets[0][1].author_id)
    # print(".attachments): ", tweets[0][1].attachments)
    # print(".context_annotations): ", tweets[0][1].context_annotations)
    # print(".conversation_id): ", tweets[0][1].conversation_id)
    # print(".edit_controls): ", tweets[0][1].edit_controls)
    # print(".edit_history_tweet_ids): ", tweets[0][1].edit_history_tweet_ids)
    # print(".entities): ", tweets[0][1].entities)
    # print(".geo): ", tweets[0][1].geo)
    # print(".in_reply_to_user_id): ", tweets[0][1].in_reply_to_user_id)
    # print(".lang): ", tweets[0][1].lang)
    # print(".possibly_sensitive): ", tweets[0][1].possibly_sensitive)
    # print(".public_metrics): ", tweets[0][1].public_metrics)
    # print(".referenced_tweets): ", tweets[0][1].referenced_tweets)
    # print(".reply_settings): ", tweets[0][1].reply_settings)
    # print(".source): ", tweets[0][1].source)
    # print(".withheld): ", tweets[0][1].withheld)


with ConnectorSnowflake() as session:
    query = (
        session.query(
            TweetModel.id,
            TweetModel.text,
            func.count(distinct(ContextAnnotationsDomainModel.id)).label('num_cad'),
            func.count(distinct(ContextAnnotationsEntityModel.id)).label('num_cae'),
            func.count(distinct(AttachmentsPoll.id)).label('num_ap'),
            func.count(distinct(AttachmentsMedia.id)).label('num_am'),
            func.count(distinct(EntitiesAnnotationsModel.id)).label('num_ea'),
            func.count(distinct(EntitiesCashtagsModel.id)).label('num_ec'),
            func.count(distinct(EntitiesHashtagsModel.id)).label('num_eh'),
            func.count(distinct(EntitiesMentionsModel.id)).label('num_em'),
            func.count(distinct(EntitiesUrlsModel.id)).label('num_eu'),
            func.count(distinct(ReferencedTweetsModel.id)).label('num_rt')
        )
        .join(ContextAnnotationsDomainModel, TweetModel.id == ContextAnnotationsDomainModel.tweet_id, isouter=True)
        .join(ContextAnnotationsEntityModel, TweetModel.id == ContextAnnotationsEntityModel.tweet_id, isouter=True)
        .join(AttachmentsPoll, TweetModel.id == AttachmentsPoll.tweet_id, isouter=True)
        .join(AttachmentsMedia, TweetModel.id == AttachmentsMedia.tweet_id, isouter=True)
        .join(EntitiesAnnotationsModel, TweetModel.id == EntitiesAnnotationsModel.tweet_id, isouter=True)
        .join(EntitiesCashtagsModel, TweetModel.id == EntitiesCashtagsModel.tweet_id, isouter=True)
        .join(EntitiesHashtagsModel, TweetModel.id == EntitiesHashtagsModel.tweet_id, isouter=True)
        .join(EntitiesMentionsModel, TweetModel.id == EntitiesMentionsModel.tweet_id, isouter=True)
        .join(EntitiesUrlsModel, TweetModel.id == EntitiesUrlsModel.tweet_id, isouter=True)
        .join(ReferencedTweetsModel, TweetModel.id == ReferencedTweetsModel.tweet_id, isouter=True)
        .group_by(TweetModel.id, TweetModel.text)
    )

    # Execute a consulta e obtenha os resultados
    results = query.all()

    # Você pode iterar pelos resultados para acessar os valores
    for row in results:
        print(
            f"ID: {row.id}, Texto: {row.text}, "
            # f"num_cad: {row.num_cad}, num_cae: {row.num_cae}, "
            # f"num_ap: {row.num_ap}, num_am: {row.num_am}, "
            # f"num_ea: {row.num_ea}, num_ec: {row.num_ec}, "
            # f"num_eh: {row.num_eh}, num_em: {row.num_em}, "
            # f"num_eu: {row.num_eu}, num_rt: {row.num_rt}"
        )


if __name__ == '__main__':
    get_tweets()
