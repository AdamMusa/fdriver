import os
import typer
import shutil
import subprocess
from .generator import files

app = typer.Typer()


# command to create project
@app.command(help="Allowed you to create project")
def init(name: str=typer.Option(
        "", help="start project.", autocompletion=complete_name
    )):

    create_folder(name)
    for i in range(2):
        with open(f"./{list(files.keys())[i]}", 'w') as file:
            if i==0:
                file.write(str(files[list(files.keys())[i]]).format(name))
            else:
                file.write(files[list(files.keys())[i]])
    create_files(name, files)

    typer.secho(f"Created project {name} successfully 🎉🎉🎉.\ncd {name}", fg=typer.colors.GREEN)


# command to start to create app modular
@app.command(help="To start to application in your project")
def startapp(name: str=typer.Option(
        "", help="startapp.", autocompletion=complete_name
    )):
    create_folder(name)
    create_files(name, files)
    typer.echo(f"Created module {name} successfully 🎉🎉🎉", fg=typer.colors.GREEN)


# command to remove app
@app.command(help="Remove application")
def remove(name: str=typer.Option(
        "", help="for removing file.", autocompletion=complete_name
    )):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), name))
        typer.echo(f"Removed successfully {name}")
    except FileNotFoundError:
        typer.echo("No such file or directory")


#allow to run fastapi server
@app.command(help="Run a FastAPI server.")
def run(prod: bool = typer.Option(False)=typer.Option(
        "", help="allowed you to start easily your server.", autocompletion=complete_name
    )):
    args = []
    if not prod:
        args.append("--reload")
    app_file = os.getenv("FASTAPI_APP", "server")
    subprocess.call(["uvicorn", f"{app_file}:app", *args])
    
    
# create folders
def create_folder(name):
    os.mkdir(os.path.join(os.getcwd(), name))
    os.mkdir(os.path.join(os.getcwd(), name+f"/{name}"))
    


# create some files
def create_files(name, files):
    with open(f"./{name}/{name}/__init__.py", 'w') as file:
        pass
    for i in range(2, (len(files))):
        with open(f"./{name}/{list(files.keys())[i]}", 'w') as file:
            file.write(files[list(files.keys())[i]])


valid_names = ["init", "startapp", "run","remove"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion

if __name__ == "__main__":
    app()
