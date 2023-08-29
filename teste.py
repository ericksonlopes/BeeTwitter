import tweepy

from config.settings import bearer_token, access_token, access_token_secret

client = tweepy.Client(bearer_token=bearer_token, consumer_key="ODQxT0gzY0JPSjJCTVl5ODAzdHI6MTpjaQ",
                       consumer_secret="Qoo7tqEZbYz0Du6wtgep1jORzEmu-3SNFHub9Ei-XbS1Szrpas",
                       access_token=access_token, access_token_secret=access_token_secret)

# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# api = tweepy.API(auth)

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# api = tweepy.API(auth)


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


if __name__ == '__main__':
    get_tweets()
