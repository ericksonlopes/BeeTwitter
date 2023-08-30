from datetime import datetime

from src.controllers.api_v2_controller import TwitterAPIV2
from src.repository.connect import Connector
from src.repository.models import TweetModel, ContextAnnotationsDomainModel, ContextAnnotationsEntityModel

api = TwitterAPIV2()
api.user(_id='jairbolsonaro')
