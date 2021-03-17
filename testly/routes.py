#implement here your routes

from fastapi import APIRouter
from testly.views import aboutView

router = APIRouter()

@router.get("/about")
async def aboutPage():
    return await aboutView()

#You can also create your method withou async keywork then you can call your method withou await
# @router.get("/")
# def aboutPage():
#     return aboutView()