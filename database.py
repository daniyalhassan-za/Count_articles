from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL = "sqlite:///./count_article.db"

engine = create_engine(URL, connect_args={"check_same_thread" : False})
sessionLocal = sessionmaker(autocommit = False, bind=engine)
Base = declarative_base()