from fastapi import FastAPI
from database import Base, engine
from api.user_api import user_router
from api.product_api import product_rout

app = FastAPI(docs_url="/")

Base.metadata.create_all(engine)

app.include_router(user_router)
app.include_router(product_rout)

