from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    username: str
    password: str

class ProductSchema(BaseModel):
    pr_name: str
    pr_description: str
    pr_quantity: int
    pr_price: float

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class CartBase(BaseModel):
    product_id: int
    quantity: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True






