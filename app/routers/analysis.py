from xml.dom.minidom import Text
from fastapi import APIRouter, Request, Form, Depends
from db.crud import get_sentiment
from db.crud import create_sentiment
from sentiment_analysis import sentiment
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from routers import templates
from dependencies import get_db
from db import schemas, crud
router = APIRouter()


# class SentimentTextData(BaseModel):
#     text: str


@router.post("/analyse", response_model=schemas.Sentiment)
async def analyse(request: Request, db: Session = Depends(get_db), text: str = Form()):
    analysed = sentiment.analyzer.analyze_sentiment(text)
    create_sentiment(db, analysed)
    redirect_url = request.url_for('analysis_result')
    response = RedirectResponse(redirect_url, status_code=303)
    return response


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/result")
async def analysis_result(request: Request, db: Session = Depends(get_db)):
    sentiment = get_sentiment(db)
    return templates.TemplateResponse("main.html", {"request": request, "sentiment": sentiment.text})
