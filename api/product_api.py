from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from database.models import Product
from schemas import ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
