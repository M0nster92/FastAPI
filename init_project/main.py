from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exception import StoryException

from router import user, article
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

@app.get('/')
def index():
    return {'message':'home page'}

@app.exception_handler(StoryException)
def story_exception_handler(request:Request, exce: StoryException):
    return JSONResponse(status_code=418, content={'detail':exce.name})

models.Base.metadata.create_all(engine)