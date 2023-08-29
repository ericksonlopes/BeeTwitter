from sqlalchemy import Column, String, DateTime, Integer, Boolean

from src.repository.connect import Base


class TweetModel(Base):
    __tablename__ = 'Tweets'

    id = Column(String, primary_key=True)
    text = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=True)
    referenced_tweets = Column(String, nullable=True)
    entites = Column(String, nullable=True)
    author_id = Column(Integer, nullable=True)
    attachments = Column(String, nullable=True)
    context_annotations = Column(String, nullable=True)
    conversation_id = Column(Integer, nullable=True)
    geo = Column(String, nullable=True)
    in_reply_to_user_id = Column(String, nullable=True)
    lang = Column(String, nullable=True)
    possibly_sensitive = Column(Boolean, nullable=True)
    promoted_metrics = Column(String, nullable=True)
    reply_settings = Column(String, nullable=True)
    source = Column(String, nullable=True)
    withheld = Column(String, nullable=True)

    # public_metrics
    retweet_count = Column(Integer, nullable=True)
    reply_count = Column(Integer, nullable=True)
    like_count = Column(Integer, nullable=True)
    quote_count = Column(Integer, nullable=True)
    bookmark_count = Column(Integer, nullable=True)
    impression_count = Column(Integer, nullable=True)

    # edit_controls
    edits_remaining = Column(String, nullable=True)
    is_edit_eligible = Column(String, nullable=True)
    editable_until = Column(DateTime, nullable=True)
    edit_history_tweet_ids = Column(String, nullable=True)

    # meta
    result_count = Column(Integer, nullable=True)
    newest_id = Column(String, nullable=True)
    oldest_id = Column(String, nullable=True)
    next_token = Column(String, nullable=True)
    includes = Column(String, nullable=True)


