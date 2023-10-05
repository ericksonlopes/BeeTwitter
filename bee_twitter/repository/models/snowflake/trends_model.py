from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, Sequence

from bee_twitter.repository.connect_snowflake import Base


class TrendModel(Base):
    __tablename__ = 'trends'

    id = Column(Integer, Sequence('TRENDS_SEQ'), primary_key=True, doc="ID na base de dados")

    hashtag = Column(String, nullable=True)
    analyzed_tweets = Column(String, nullable=True)
    order = Column(Integer, nullable=True)

    dt_creation = Column(DateTime, nullable=True, default=datetime.now())
    dt_update = Column(DateTime, nullable=True, default=datetime.now())
    dt_expiration = Column(DateTime, nullable=True)
    cod_status = Column(Integer, nullable=True, default=1)
