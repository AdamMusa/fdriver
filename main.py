import os
import typer
from generator import files

app = typer.Typer()

#command to create project
@app.command()
def init(name: str):
    
    create_folder(name)
    for i in range(2):
        with open(f"./{list(files.keys())[i]}",'w') as file:
            file.write(files[list(files.keys())[i]])
    create_files(name,files)
    
    typer.echo(f"Created project {name} successfully.\ncd {name}")

#command to start to create app modular
@app.command()
def startapp(name: str):
    create_folder(name)
    create_files(name,files)
    typer.echo(f"Created module {name} successfully")

#create folders
def create_folder(name):
    os.mkdir(os.path.join(os.getcwd(),name))
    os.mkdir(os.path.join(os.getcwd(),name+f"/{name}"))

#create some files
def create_files(name,files):
    with open(f"./{name}/{name}/__init__.py",'w') as file:
        pass
    for i in range(2,(len(files))):
        with open(f"./{name}/{list(files.keys())[i]}",'w') as file:
            file.write(files[list(files.keys())[i]])

if __name__ =="__main__" :
    app()