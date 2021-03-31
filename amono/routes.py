#implement your routes here
from fastapi import APIRouter
from .views import aboutView

router_amono = APIRouter()

# @router_amono.get("/about")
# def aboutRoute():
#     return aboutView()

router_amono.get("/about", lambda: aboutView())
