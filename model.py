# from sqlalchemy import Column, Integer, String, ForeignKey
# from database import Base
# from sqlalchemy.orm import relationship








# class User(Base):
#     __tablename__ = 'user'

#     First_name = Column(String, nullable=False)
#     Last_name = Column(String, nullable= False )
#     user_name = Column(String, unique=True, nullable=False)
#     Email = Column(String )
#     Password = Column(String, unique=True)

#     artricle = relationship("Article", back_populates="user")

# class Article(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
#     title = Column(String, nullable=False)
#     user_name = Column(String, ForeignKey("user.user_name")) 

#     user =  relationship("User", back_populates="articles")  


# model.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True) 
    First_name = Column(String, nullable=False)
    Last_name = Column(String, nullable=False)
    user_name = Column(String, unique=True, nullable=False) 
    Email = Column(String, unique=True, nullable=False)
    Password = Column(String, nullable=False)

    articles = relationship("Article", back_populates="user")


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    user_name = Column(String, ForeignKey("user.user_name"), nullable=False)

    user = relationship("User", back_populates="articles")
