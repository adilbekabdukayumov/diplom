from pydantic import BaseModel
from pydantic import BaseModel

# ===== User schemas =====
class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# ===== User schemas =====
class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# ===== Product schemas =====
class ProductCreate(BaseModel):
    pr_name: str
    pr_description: str
    pr_price: int
    pr_quantity: int


class ProductRead(ProductCreate):
    id: int

    class Config:
        orm_mode = True

# ===== Category schemas =====
class CategoryCreate(BaseModel):
    name: str

class CategoryRead(CategoryCreate):
    id: int

    class Config:
        orm_mode = True

# ===== Cart schemas =====
class CartCreate(BaseModel):
    product_id: int
    quantity: int

class CartRead(CartCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True
