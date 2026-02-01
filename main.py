from fastapi import FastAPI

from api import product_api, user_api
from routers import categories, cart

app = FastAPI()

app.include_router(product_api.router)
app.include_router(user_api.router)
app.include_router(categories.router)
app.include_router(cart.router)
