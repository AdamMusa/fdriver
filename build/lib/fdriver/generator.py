files = {
"server.py":"""#implement your routes here
from fastapi import FastAPI
from {}.views import home

app = FastAPI()

@app.get("/")
async def homePage():
    return await home()

#You can also create your method withou async keywork then you can call your method withou await
# @app.get("/")
# def homePage():
#     return home()

""",
"settings.py": """#configuration for database""",
"test.py":"""#implement your test here""",
"models.py": """#implement your routes here
from pydantic import BaseModel""",
    
"views.py":"""#implement your views here

async def home():
    return {"Welcome":"To HomePage"}
    
#You can also create your method withou async keyword 
# def home():
#     return {"Welcome":"To HomePage"}
    
""",
}

