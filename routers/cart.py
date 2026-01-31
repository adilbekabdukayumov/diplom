from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Cart
from schemas import CartCreate

router = APIRouter(prefix="/cart", tags=["Cart"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}")
def add_to_cart(user_id: int, item: CartCreate, db: Session = Depends(get_db)):
    cart_item = Cart(
        user_id=user_id,
        product_id=item.product_id,
        quantity=item.quantity
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/{user_id}")
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(Cart).filter(Cart.user_id == user_id).all()
