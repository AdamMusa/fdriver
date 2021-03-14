from fastapi import FastAPI
from .views import home

app = FastAPI()

@app.get("/")
async def homePage():
    return await home()



