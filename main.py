from fastapi import FastAPI, Depends, HTTPException
from database import sessionLocal, engine, Base
from sqlalchemy.orm import Session 
from model import Article 


Base.metadata.create_all(bind= engine)

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close()


@app.post("/api/v1/articles/")
async def create_article(id: int, tilte:str, db: Session = Depends(get_db)):
    new_article = Article(id = id, tilte = tilte) 
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return {"id": new_article.id, "title": new_article.title}


@app.get("/api/v1/articles")
async def get_article( db : Session = Depends(get_db)):
    articles = db.query(Article).all()
    if not articles:
        raise HTTPException(status_code=404, detail="No Article Found")
    return [{"id" : article.id, "title": article.title,  } for article in articles]





# from fastapi import FastAPI, Depends, HTTPException
# from database import sessionLocal, engine, Base
# from sqlalchemy.orm import Session 
# from model import Article




# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/api/v1/articles/")
# def create_article(id: int, title: str, db: Session = Depends(get_db)):
#     existing_article = db.query(Article).filter(Article.id == id).first()
#     if existing_article:
#         raise HTTPException(status_code=400, detail="Article with this ID already exists.")

#     new_article = Article(id=id, title=title)
#     db.add(new_article)
#     db.commit()
#     db.refresh(new_article)
#     return {"id": new_article.id, "title": new_article.title}

# # Endpoint to read articles
# @app.get("/api/v1/articles/")
# def read_articles(db: Session = Depends(get_db)):
#     articles = db.query(Article).all()
#     return [{"id": article.id, "title": article.title} for article in articles]


