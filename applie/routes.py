#implement here your routes

from fastapi import APIRouter
from applie.views import homeView

router = APIRouter()

@router.get("/")
async def homePage():
    return await homeView()

#You can also create your method withou async keywork then you can call your method withou await
# @router.get("/")
# def homePage():
#     return homeView()