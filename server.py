#Import all your routes here

from applie.routes import router
from testly import routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)
app.include_router(routes.router)
