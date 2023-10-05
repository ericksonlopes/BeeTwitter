from bee_twitter.repository.connect_snowflake import engine

from bee_twitter.repository.models.snowflake import *

Base.metadata.create_all(engine)
