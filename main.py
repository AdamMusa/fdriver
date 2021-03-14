import os
import typer
from generator import files

app = typer.Typer()
@app.command()
def init(name: str):
    os.mkdir(os.path.join(os.getcwd(),name))
    os.mkdir(os.path.join(os.getcwd(),name+f"/{name}"))
    for i in range(2):
        with open(f"./{list(files.keys())[i]}",'w') as file:
            file.write(files[list(files.keys())[i]])
    with open(f"./{name}/{name}/__init__.py",'w') as file:
        pass
    for i in range(2,(len(files))):
        with open(f"./{name}/{list(files.keys())[i]}",'w') as file:
            file.write(files[list(files.keys())[i]])
    
    typer.echo(f"Created project {name} successfully.\ncd {name}")

@app.command()
def startapp(name: str):
    typer.echo(f"Created module {name} successfully")


if __name__ =="__main__" :
    app()