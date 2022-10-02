from pydantic import BaseModel


class SentimentBase(BaseModel):
    id: int
    text: str


class SentimentCreate(SentimentBase):
    pass


class Sentiment(SentimentBase):
    id: int
    text: str

    class Config:
        orm_mode = True
