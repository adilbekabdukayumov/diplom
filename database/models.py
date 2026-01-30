from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True,autoincrement=True)
    pr_name = Column(String, nullable=False)
    pr_description = Column(Text, nullable=False)
    pr_price = Column(Integer, nullable=False)
    pr_quantity = Column(Integer, nullable=False)






