from fastapi import FastAPI, Depends
from database import sessionLocal, engine, Base
from sqlalchemy.orm import Session 
from model import Article
from typing  import List

app = FastAPI()

Base.metadata.create_all(bind= engine)

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close()


initial_articles = [
    {"id" : 1, "title": "What is Fastapi: Chapter 1 [Introduction]", "content": "Introduction"},
    {"id" : 2, "title": "What is Fastapi: Chapter 2 [Introduction]", "content": "Introduction"},
    {"id" : 3, "title": "What is Fastapi: Chapter 3 [Introduction]", "content": "Introduction"},
    {"id" : 4, "title": "What is Fastapi: Chapter 4 [Introduction]", "content": "Introduction"},
    {"id" : 5, "title": "What is Fastapi: Chapter 5 [Introduction]", "content": "Introduction"},
    {"id" : 6, "title": "What is Fastapi: Chapter 6 [Introduction]", "content": "Introduction"},
    {"id" : 7, "title": "What is Fastapi: Chapter 7 [Introduction]", "content": "Introduction"},
    {"id" : 8, "title": "What is Fastapi: Chapter 8 [Introduction]", "content": "Introduction"},
    {"id" : 9, "title": "What is Fastapi: Chapter 9 [Introduction]", "content": "Introduction"},
    {"id" : 10, "title": "What is Fastapi: Chapter 10 [Introduction]", "content": "Introduction"},
    {"id" : 11, "title": "What is Fastapi: Chapter 11 [Introduction]", "content": "Introduction"},
    {"id" : 12, "title": "What is Fastapi: Chapter 12 [Introduction]", "content": "Introduction"},
    {"id" : 13, "title": "What is Fastapi: Chapter 13 [Introduction]", "content": "Introduction"},
    {"id" : 14, "title": "What is Fastapi: Chapter 14 [Introduction]", "content": "Introduction"},
    {"id" : 15, "title": "What is Fastapi: Chapter 15 [Introduction]", "content": "Introduction"},
    {"id" : 16, "title": "What is Fastapi: Chapter 16 [Introduction]", "content": "Introduction"},
    {"id" : 17, "title": "What is Fastapi: Chapter 17 [Introduction]", "content": "Introduction"},
    {"id" : 18, "title": "What is Fastapi: Chapter 18 [Introduction]", "content": "Introduction"},
]


@app.on_event("add-articles")
async def add_articles():
    db = sessionLocal()
    existing_articles = db.query()
    for article in initial_articles:
        db_articles = Article(**article)
        db.add(db_articles)
        db.commit()
        db.refresh(db_articles)
        return db_articles

@app.post("/api/v1/articles/", response_model=Article)
async def add_article(article : Article, db: Session = Depends(get_db)):
    db.add(article)
    db.commit()
    db.refresh(article)
    return article









@app.get("/api/v1/articles")
async def  get_articles():
    articles =  [
        {"id" : 1, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 2, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 3, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 4, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 5, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 6, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 7, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 7, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 8, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 9, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 10, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 11, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 12, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 13, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 14, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 15, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 16, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 17, "title": "What is Fastapi : Chapter 1 [introduction]"},
        {"id" : 18, "title": "What is Fastapi : Chapter 1 [introduction]"},

    ]
    return articles