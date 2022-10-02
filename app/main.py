from fastapi import FastAPI, Request
from routers.analysis import router as analysis_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(analysis_router)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
