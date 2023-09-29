from bee_twitter.repository.connect import engine

from bee_twitter.repository.models import *

Base.metadata.create_all(engine)
