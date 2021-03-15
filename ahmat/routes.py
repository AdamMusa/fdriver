#implement your routes here
from fastapi import FastAPI
from .views import home

app = FastAPI()

@app.get("/")
async def homePage():
    return await home()

#You can also create your method withou async keywork then you can call your method withou await
# @app.get("/")
# def homePage():
#     return home()


