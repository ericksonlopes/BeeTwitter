from sqlalchemy import distinct, func

from bee_twitter.config.settings import API_KEY_OPENAI
from bee_twitter.controllers.api_v2_controller import TwitterAPIV2
from bee_twitter.controllers.political_tweet_analyzer import PoliticalTweetAnalyzerController
from bee_twitter.repository.connect import Connector
from bee_twitter.repository.models import *

api = TwitterAPIV2()
api.user(_id='jairbolsonaro')

api_key = API_KEY_OPENAI
pta = PoliticalTweetAnalyzerController(api_key)
pta.run()

# with Connector() as session:
#     query = (
#         session.query(
#             TweetModel.id,
#             TweetModel.text,
#             func.count(distinct(ContextAnnotationsDomainModel.id)).label('num_cad'),
#             func.count(distinct(ContextAnnotationsEntityModel.id)).label('num_cae'),
#             func.count(distinct(AttachmentsPoll.id)).label('num_ap'),
#             func.count(distinct(AttachmentsMedia.id)).label('num_am'),
#             func.count(distinct(EntitiesAnnotationsModel.id)).label('num_ea'),
#             func.count(distinct(EntitiesCashtagsModel.id)).label('num_ec'),
#             func.count(distinct(EntitiesHashtagsModel.id)).label('num_eh'),
#             func.count(distinct(EntitiesMentionsModel.id)).label('num_em'),
#             func.count(distinct(EntitiesUrlsModel.id)).label('num_eu'),
#             func.count(distinct(ReferencedTweetsModel.id)).label('num_rt')
#         )
#         .join(ContextAnnotationsDomainModel, TweetModel.id == ContextAnnotationsDomainModel.tweet_id, isouter=True)
#         .join(ContextAnnotationsEntityModel, TweetModel.id == ContextAnnotationsEntityModel.tweet_id, isouter=True)
#         .join(AttachmentsPoll, TweetModel.id == AttachmentsPoll.tweet_id, isouter=True)
#         .join(AttachmentsMedia, TweetModel.id == AttachmentsMedia.tweet_id, isouter=True)
#         .join(EntitiesAnnotationsModel, TweetModel.id == EntitiesAnnotationsModel.tweet_id, isouter=True)
#         .join(EntitiesCashtagsModel, TweetModel.id == EntitiesCashtagsModel.tweet_id, isouter=True)
#         .join(EntitiesHashtagsModel, TweetModel.id == EntitiesHashtagsModel.tweet_id, isouter=True)
#         .join(EntitiesMentionsModel, TweetModel.id == EntitiesMentionsModel.tweet_id, isouter=True)
#         .join(EntitiesUrlsModel, TweetModel.id == EntitiesUrlsModel.tweet_id, isouter=True)
#         .join(ReferencedTweetsModel, TweetModel.id == ReferencedTweetsModel.tweet_id, isouter=True)
#         .group_by(TweetModel.id, TweetModel.text)
#     )
#
#     # Execute a consulta e obtenha os resultados
#     results = query.all()
#
#     # Você pode iterar pelos resultados para acessar os valores
#     for row in results:
#         print(
#             f"ID: {row.id}, Texto: {row.text}, "
#             # f"num_cad: {row.num_cad}, num_cae: {row.num_cae}, "
#             # f"num_ap: {row.num_ap}, num_am: {row.num_am}, "
#             # f"num_ea: {row.num_ea}, num_ec: {row.num_ec}, "
#             # f"num_eh: {row.num_eh}, num_em: {row.num_em}, "
#             # f"num_eu: {row.num_eu}, num_rt: {row.num_rt}"
#         )
