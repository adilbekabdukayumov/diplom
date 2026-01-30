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






