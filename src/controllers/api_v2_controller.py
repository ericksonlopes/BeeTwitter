from src.repository.models.tweets_model import TweetModel
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

            list_tweets = []
            for tweet in data:
                tweet_model = TweetModel(
                    id=tweet['id'],
                    text=tweet['text'],
                    created_at=tweet['created_at'],
                    retweet_count=tweet['public_metrics']['retweet_count'],
                    reply_count=tweet['public_metrics']['reply_count'],
                    like_count=tweet['public_metrics']['like_count'],
                    quote_count=tweet['public_metrics']['quote_count'],
                    bookmark_count=tweet['public_metrics']['bookmark_count'],
                    impression_count=tweet['public_metrics']['impression_count'],
                    referenced_tweets=tweet['referenced_tweets'],
                    entites=str(tweet['entities']),
                    author_id=tweet['author_id'],
                    attachments=str(tweet['attachments']),
                    context_annotations=str(tweet['context_annotations']),
                    conversation_id=tweet['conversation_id'],
                    edits_remaining=tweet['edit_controls']['edits_remaining'],
                    is_edit_eligible=tweet['edit_controls']['is_edit_eligible'],
                    editable_until=tweet['edit_controls']['editable_until'],
                    edit_history_tweet_ids=str(tweet['edit_history_tweet_ids']),
                    geo=str(tweet['geo']),
                    in_reply_to_user_id=tweet['in_reply_to_user_id'],
                    lang=tweet['lang'],
                    possibly_sensitive=tweet['possibly_sensitive'],
                    promoted_metrics=str(tweet['promoted_metrics']),
                    reply_settings=tweet['reply_settings'],
                    source=tweet['source'],
                    withheld=str(tweet['withheld']),

                    # meta
                    result_count=meta['result_count'],
                    newest_id=meta['newest_id'],
                    oldest_id=meta['oldest_id'],
                    next_token=meta['next_token'],

                    # includes
                    includes=str(includes)
                )

                list_tweets.append(tweet_model)

            # with Connector() as session:
            #     session.add(user)

        except Exception as error:
            print(error)
            return False

        for item in list_tweets:
            print(item.__dict__)
            print("*" * 100)
        return True


if __name__ == '__main__':
    api = TwitterAPIV2()
    api.user(_id='jairbolsonaro')

    # .text):  Parabéns para a Central Única dos Trabalhadores pelos seus 40 anos. https://t.co/Gk6jchXwr1
    # .id):  1696309169857429677
    # .created_at):  2023-08-28 23:49:56+00:00
    # .public_metrics):  {'retweet_count': 613, 'reply_count': 308, 'like_count': 3749, 'quote_count': 13, 'bookmark_count': 14, 'impression_count': 171212}
    # .entities):  {'urls': [{'start': 68, 'end': 91, 'url': 'https://t.co/Gk6jchXwr1', 'expanded_url': 'https://twitter.com/inst_lula/status/1696238419230228515', 'display_url': 'twitter.com/inst_lula/stat…'}], 'annotations': [{'start': 16, 'end': 46, 'probability': 0.5927, 'type': 'Other', 'normalized_text': 'Central Única dos Trabalhadores'}]}
    # .author_id):  2670726740
    # .attachments):  None
    # .context_annotations):  [{'domain': {'id': '10', 'name': 'Person', 'description': 'Named people in the world like Nelson Mandela'}, 'entity': {'id': '862070591737675776', 'name': 'Luiz Inácio "Lula" da Silva', 'description': 'Brazilian 35th president.'}}, {'domain': {'id': '29', 'name': 'Events [Entity Service]', 'description': 'Real world events. '}, 'entity': {'id': '1411038381841084418', 'name': 'Brazil General Elections 2022', 'description': 'Brazil General Elections 2022 (presidential, gubernatorial, VPS)'}}, {'domain': {'id': '35', 'name': 'Politician', 'description': 'Politicians in the world, like Joe Biden'}, 'entity': {'id': '862070591737675776', 'name': 'Luiz Inácio "Lula" da Silva', 'description': 'Brazilian 35th president.'}}, {'domain': {'id': '38', 'name': 'Political Race', 'description': ''}, 'entity': {'id': '1411038381841084418', 'name': 'Brazil General Elections 2022', 'description': 'Brazil General Elections 2022 (presidential, gubernatorial, VPS)'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '847878884917886977', 'name': 'Politics', 'description': 'Politics'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '862070591737675776', 'name': 'Luiz Inácio "Lula" da Silva', 'description': 'Brazilian 35th president.'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1070032753834438656', 'name': 'Political figures', 'description': 'Politician'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1411038381841084418', 'name': 'Brazil General Elections 2022', 'description': 'Brazil General Elections 2022 (presidential, gubernatorial, VPS)'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1455305940291375106', 'name': 'Brazil politics'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1488973753274929152', 'name': 'Political events'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1518653237720625152', 'name': 'Brazil political figures'}}, {'domain': {'id': '131', 'name': 'Unified Twitter Taxonomy', 'description': 'A taxonomy of user interests. '}, 'entity': {'id': '1518940800985427968', 'name': 'Brazil political events'}}]
    # .conversation_id):  1696309169857429677
    # .edit_controls):  {'edits_remaining': 5, 'is_edit_eligible': True, 'editable_until': datetime.datetime(2023, 8, 29, 0, 49, 56, tzinfo=datetime.timezone.utc)}
    # .edit_history_tweet_ids):  [1696309169857429677]
    # .entities):  {'urls': [{'start': 68, 'end': 91, 'url': 'https://t.co/Gk6jchXwr1', 'expanded_url': 'https://twitter.com/inst_lula/status/1696238419230228515', 'display_url': 'twitter.com/inst_lula/stat…'}], 'annotations': [{'start': 16, 'end': 46, 'probability': 0.5927, 'type': 'Other', 'normalized_text': 'Central Única dos Trabalhadores'}]}
    # .geo):  None
    # .in_reply_to_user_id):  None
    # .lang):  pt
    # .possibly_sensitive):  False
    # .public_metrics):  {'retweet_count': 613, 'reply_count': 308, 'like_count': 3749, 'quote_count': 13, 'bookmark_count': 14, 'impression_count': 171212}
    # .referenced_tweets):  [<ReferencedTweet id=1696238419230228515 type=quoted>]
    # .reply_settings):  everyone
    # .source):  None
    # .withheld):  None
