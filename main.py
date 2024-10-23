from fastapi import FastAPI

app = FastAPI()


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