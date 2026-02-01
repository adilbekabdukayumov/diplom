from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    pr_name = Column(String, nullable=False)
    pr_description = Column(Text, nullable=False)
    pr_price = Column(Integer, nullable=False)
    pr_quantity = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))  # 🔥 МІНЕ ОСЫ
    category = relationship("Category", back_populates="products")



class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    user = relationship("User")
    product = relationship("Product")






