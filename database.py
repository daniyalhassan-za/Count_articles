from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL = "sqlite:///./check_articles.db"

engine = create_engine(URL)
sesion = sessionmaker(autocommit = False, bind=engine)
Base = declarative_base()