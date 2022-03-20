from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models


class RepositorioNews:
    def __init__(self, session: Session):
        self.session = session

    def criar_news(self, news):
        db_news = models.News(
            id=news['id'],
            feature=news['featured'],
            title=news['title'],
            url=news['url'],
            imageUrl=news['imageUrl'],
            newsSite=news['newsSite'],
            summary=news['summary'],
            publishedAt=news['publishedAt'],
            launches_id=news['launches_id'],
            launches_provider=news['launches_provider'],
            events_id=news['events_id'],
            events_provider=news['events_provider'],
            )

        self.session.add(db_news)
        self.session.commit()
        self.session.refresh(db_news)
        return db_news
