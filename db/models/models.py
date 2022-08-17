from sqlalchemy import (Column, Integer,
String, Boolean, Date, ForeignKey)
from sqlalchemy.orm import relationship

from db.base_class import Base


class Users(Base):
    id = Column(Integer,primary_key=True, index=True)
    uname = Column(String, nullable=False)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    date_created = Column(Integer, nullable=False)
    bookmark_rel = relationship("Bookmarks", back_populates="user_rel")

class News(Base):
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    posted_on = Column(Integer, nullable=False)
    bookmark_rel = relationship("Bookmarks", back_populates="news_rel")


class Bookmarks(Base):
    id = Column(Integer,primary_key=True, index=True)
    user = Column(Integer, ForeignKey("users.id"))
    news = Column(Integer, ForeignKey("news.id"))
    user_rel = relationship("Users", back_populates="bookmark_rel")
    news_rel = relationship("News", back_populates="bookmark_rel")
