from fastapi import FastAPI
from database import Base, engine
from api.user_api import user_router
from routers import products
from routers import categories, cart

app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(user_router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(cart.router)


