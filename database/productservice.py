from database.models import Product
from schemas import ProductSchema
from database import Base, get_db


def get_exact_product(product_id):
    db = next(get_db())
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return {"status": False, "message": "Product not found"}
    else:
        return {"status": True, "product": product}

def get_all_product():
    db = next(get_db())
    products = db.query(Product).all()
    if not products:
        return {"status": False, "message": "No products found"}
    else:
        return {"status": True, "products": products}

def create_product(product: ProductSchema):
    db= next(get_db())
    prod_data = product.model_dump()
    new_product = Product(**prod_data)
    db.add(new_product)
    db.commit()
    return True

def update_product(pid,change_data, new_data):
    db= next(get_db())
    exact_product = get_exact_product(pid)
    if exact_product:
        if change_data == 'pr_name':
            exact_product.pr_name = new_data
        elif change_data == 'pr_price':
            exact_product.pr_price = new_data
        elif change_data == 'pr_quantity':
            exact_product.pr_quantity = new_data
        elif change_data == 'pr_amount':
            exact_product.pr_amount = new_data
        else:
            return False
        db.commit()
        return True
    return False


def delete_product(pid):
    db = next(get_db())
    pr_to_delete = db.query(Product).filter(Product.id == pid).first()
    if pr_to_delete:
        db.delete(pr_to_delete)
        db.commit()
        return True
    return False



