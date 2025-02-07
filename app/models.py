from sqlalchemy import Column, Integer, String
from app.databse import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class User(Base):
    __tablename__ = "users"
    id=Column(Integer,primary_key=True, index=True)
    name= Column(String, index= True)
    email=Column(String, unique=True, index=True)