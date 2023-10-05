from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey, Sequence, Float
from sqlalchemy.orm import relationship

from bee_twitter.repository.connect_snowflake import Base


class TweetModel(Base):
    __tablename__ = 'Tweets'

    id = Column(Integer, Sequence('TWEETS_SEQ'), primary_key=True, doc="ID na base de dados")
    id_tweet = Column(Integer, nullable=True, doc="ID do tweet")
    text = Column(String, nullable=True, doc="Texto do tweet")
    created_at = Column(DateTime, nullable=True, doc="Data e hora de criação do tweet")

    url = Column(String, nullable=True)
    author_id = Column(Integer, nullable=True)
    conversation_id = Column(Integer, nullable=True)
    geo = Column(String, nullable=True)
    in_reply_to_user_id = Column(String, nullable=True)
    lang = Column(String, nullable=True)
    possibly_sensitive = Column(Boolean, nullable=True)
    promoted_metrics = Column(String, nullable=True)
    reply_settings = Column(String, nullable=True)
    source = Column(String, nullable=True)
    withheld = Column(String, nullable=True)
    ind_analysis = Column(Boolean, default=False, doc="Indicador de análise do tweet")

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

    # includes
    includes = Column(String, nullable=True)

    # Context_annotations
    context_annotations_domain = relationship("ContextAnnotationsDomainModel", back_populates="tweet")
    context_annotations_entity = relationship("ContextAnnotationsEntityModel", back_populates="tweet")
    entities_mentions = relationship("EntitiesMentionsModel", back_populates="tweet")
    entities_annotations = relationship("EntitiesAnnotationsModel", back_populates="tweet")
    entities_cashtags = relationship("EntitiesCashtagsModel", back_populates="tweet")
    entities_hashtags = relationship("EntitiesHashtagsModel", back_populates="tweet")
    entities_urls = relationship("EntitiesUrlsModel", back_populates="tweet")
    referenced_tweets = relationship("ReferencedTweetsModel", back_populates="tweet")
    attachments_poll = relationship("AttachmentsPoll", back_populates="tweet")
    attachments_media = relationship("AttachmentsMedia", back_populates="tweet")


class ContextAnnotationsDomainModel(Base):
    __tablename__ = 'ContextAnnotationsDomain'

    id = Column(Integer, Sequence('CONTEXT_ANNOTATIONS_ENTITY_SEQ'), primary_key=True)
    id_domain = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="context_annotations_domain")


class ContextAnnotationsEntityModel(Base):
    __tablename__ = 'ContextAnnotationsEntity'

    id = Column(Integer, Sequence('CONTEXT_ANNOTATIONS_ENTITY_SEQ'), primary_key=True)
    id_entity = Column(String)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="context_annotations_entity")


class EntitiesMentionsModel(Base):
    __tablename__ = 'EntitiesMentions'

    id = Column(Integer, Sequence('ENTITIESMENTIONS_SEQ'), primary_key=True)
    start = Column(Integer, nullable=True)
    end = Column(Integer, nullable=True)
    tag = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="entities_mentions")


class EntitiesAnnotationsModel(Base):
    __tablename__ = 'EntitiesAnnotations'

    id = Column(Integer, Sequence('ENTITIESANNOTATIONS_SEQ'), primary_key=True)
    start = Column(Integer, nullable=True)
    end = Column(Integer, nullable=True)
    probability = Column(Float, nullable=True)
    type = Column(String, nullable=True)
    normalized_text = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="entities_annotations")


class EntitiesCashtagsModel(Base):
    __tablename__ = 'EntitiesCashtags'

    id = Column(Integer, Sequence('ENTITIESCASHTAGS_SEQ'), primary_key=True)
    start = Column(Integer, nullable=True)
    end = Column(Integer, nullable=True)
    tag = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="entities_cashtags")


class EntitiesHashtagsModel(Base):
    __tablename__ = 'EntitiesHashtags'

    id = Column(Integer, Sequence('ENTITIESHASHTAGS_SEQ'), primary_key=True)
    start = Column(Integer, nullable=True)
    end = Column(Integer, nullable=True)
    tag = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="entities_hashtags")


class EntitiesUrlsModel(Base):
    __tablename__ = 'EntitiesUrls'

    id = Column(Integer, Sequence('ENTITIESURLS_SEQ'), primary_key=True)
    start = Column(Integer, nullable=True)
    end = Column(Integer, nullable=True)
    url = Column(String, nullable=True)
    expanded_url = Column(String, nullable=True)
    display_url = Column(String, nullable=True)
    status = Column(String, nullable=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    unwound_url = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="entities_urls")


class ReferencedTweetsModel(Base):
    __tablename__ = 'ReferencedTweets'

    id = Column(Integer, Sequence('REFERENCEDTWEETS_SEQ'), primary_key=True)
    type = Column(String, nullable=True)
    id_Referenced = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="referenced_tweets")


class AttachmentsPoll(Base):
    __tablename__ = 'AttachmentsPoll'

    id = Column(Integer, Sequence('ATTACHMENTSPOLL_SEQ'), primary_key=True)
    poll_id = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="attachments_poll")


class AttachmentsMedia(Base):
    __tablename__ = 'AttachmentsMedia'

    id = Column(Integer, Sequence('ATTACHMENTSMEDIA_SEQ'), primary_key=True)
    midea_key = Column(String, nullable=True)

    tweet_id = Column(String, ForeignKey('Tweets.id'))
    tweet = relationship("TweetModel", back_populates="attachments_media")
