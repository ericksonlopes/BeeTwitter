from sqlalchemy import Column, String, DateTime, Integer, Float, Sequence

from bee_twitter.repository.connect_snowflake import Base


class TweetQualityModel(Base):
    __tablename__ = 'TweetsQuality'

    id = Column(Integer, Sequence('TWEETS_QUALITY_SEQ'), primary_key=True)
    id_tweet = Column(String, nullable=True)
    text = Column(String, nullable=True)
    tweet_text = Column(String, nullable=True)
    dt_creation = Column(DateTime, nullable=True)
    dt_update = Column(DateTime, nullable=True)
    dt_expiration = Column(DateTime, nullable=True)
    url = Column(String, nullable=True)
    author_id = Column(Integer, nullable=True)
    quality_results_name = Column(String, nullable=True)
    quality_results_value = Column(Float, nullable=True)

    def __repr__(self):
        return (
            f'TweetQualityModel(id={self.id}, '
            f'id_tweet={self.id_tweet}, text={self.text}, '
            f'tweet_text={self.tweet_text},'
            f' dt_creation={self.dt_creation},'
            f' dt_update={self.dt_update}, '
            f'dt_expiration={self.dt_expiration}, '
            f'url={self.url}, '
            f'author_id={self.author_id},'
            f' quality_results_name={self.quality_results_name}, '
            f'quality_results_value={self.quality_results_value})'
        )
