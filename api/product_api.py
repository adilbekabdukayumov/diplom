from fastapi import FastAPI, APIRouter
from database.productservice import *

product_rout = APIRouter(prefix='/products', tags=['products'])

@product_rout.post('/product')
def create_prod(post: ProductSchema):
    result = create_product(post)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}

@product_rout.get('/product')
def all_list_products():
    result = get_all_product()
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}

@product_rout.delete('/product')
def delete_prod(product: ProductSchema):
    result = delete_product(product)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}

@product_rout.get('/product/<id>')
def get_product(id: int):
    result = get_exact_product(id)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}



