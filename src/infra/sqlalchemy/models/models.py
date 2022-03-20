from sqlalchemy import Column, Integer, Boolean, String

from src.infra.sqlalchemy.config.database import Base


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    feature = Column(Boolean, default=False)
    title = Column(String)
    url = Column(String)
    imageUrl = Column(String)
    newsSite = Column(String)
    summary = Column(String)
    publishedAt = Column(String)
    launches_id = Column(String)
    launches_provider = Column(String)
    events_id = Column(String)
    events_provider = Column(String)
