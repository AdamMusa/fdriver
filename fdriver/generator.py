files = {
"server.py":"""#Import all your routes here

from {}.routes import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)
""",

"settings.py": """#configuration for database""",

"test.py":"""#implement your test here""",

"models.py": """#implement your models here
from pydantic import BaseModel""",
    
"views.py":"""#implement your views here

async def homeView():
    return {"Welcome":"To HomePage"}
    
#You can also create your method withou async keyword 
# def homeView():
#     return {"Welcome":"To HomePage"}
    
""",
"routes.py":"""#implement here your routes

from fastapi import APIRouter
from {}.views import homeView

router = APIRouter()

@router.get("/")
async def homePage():
    return await homeView()

#You can also create your method withou async keywork then you can call your method withou await
# @router.get("/")
# def homePage():
#     return homeView()"""
}

app_files = {
"":"",
"":"",
"test.py":"""#implement your test here""",

"models.py": """#implement your models here
from pydantic import BaseModel""",
    
"views.py":"""#implement your views here

async def aboutView():
    return {"Welcome":"To AboutPage"}
    
#You can also create your method withou async keyword 
# def aboutView():
#     return {"Welcome":"To AboutPage"}
    
""",
"routes.py":"""#implement here your routes

from fastapi import APIRouter
from {}.views import aboutView

router_app = APIRouter()

@router.get("/about")
async def aboutPage():
    return await aboutView()

#You can also create your method withou async keywork then you can call your method withou await
# @router.get("/")
# def aboutPage():
#     return aboutView()"""
}