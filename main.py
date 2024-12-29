from fastapi import FastAPI, Depends, HTTPException
from database import sessionLocal, engine, Base
from sqlalchemy.orm import Session 
from model import Article , User


Base.metadata.create_all(bind= engine)

app = FastAPI()
def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.post("/api/v1/create_user/")
def register_user( user_name: str, First_name: str, Last_name: str, Email: str, Password: str, db: Session = Depends(get_db)):

    new_user = User( user_name = user_name, First_name = First_name, Last_name= Last_name, Email=Email, Password= Password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message" : "New User Registered Sucessfully"}

@app.post("/api/v1/articles/")
async def create_article( user_name : str, title:str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_name == user_name).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        new_article = Article(user_name = user_name, title=title)
        db.add(new_article)
        db.commit()
        db.refresh(new_article)

        return {"title": new_article.title}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/articles")
async def get_article( db : Session = Depends(get_db)):
    articles = db.query(Article).all()
    if not articles:
        raise HTTPException(status_code=404, detail="No Article Found")
    return [{"id" : article.id, "title": article.title, "User_name" : article.user_name} for article in articles]


