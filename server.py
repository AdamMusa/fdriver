#Import all your routes here

from project.routes import router
from fastapi import FastAPI
from amono.routes import router_amono

app = FastAPI()

app.include_router(router)
app.include_router(router_amono)
