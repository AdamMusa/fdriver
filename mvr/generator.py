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
home()""",
    
"views.py":"""async def home():
    return {"Welcome":"To HomePage"}""",
}

