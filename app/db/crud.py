from sqlalchemy.orm import Session

from . import models, schemas


def get_sentiment(db: Session):
    return db.query(models.Sentiment).order_by(models.Sentiment.id.desc()).first()


def create_sentiment(db: Session, sentiment: schemas.SentimentCreate):
    db_sentiment = models.Sentiment(text=sentiment)
    db.add(db_sentiment)
    db.commit()
    db.refresh(db_sentiment)
    return db_sentiment
