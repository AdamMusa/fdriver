files = {
"server.py":"""from . import routes

if __name__ =="__main__" :
    routes

""",
"database.py": """#configuration for database""",
"models.py": """from pydantic import BaseModel""",

"routes.py":
"""from fastapi import FastAPI
from .views import home

app = FastAPI()

@app.get("/")
async def homePage():
    return await home()

#You can also create your method withou async keywork then you can call your method withou await
# @app.get("/")
# def homePage():
#     return home()


""",
    
"views.py":"""async def home():
    return {"Welcome":"To HomePage"}
    
#You can also create your method withou async keyword 
# def home():
#     return {"Welcome":"To HomePage"}
    
""",
}

