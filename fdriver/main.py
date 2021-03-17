import os
import typer
import shutil
import subprocess
from fdriver.generator import files,app_files

app = typer.Typer()

valid_names = ["init", "startapp", "run","remove"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion


# command to create project
@app.command(help="To create a new Project")
def init(name: str):

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
@app.command(help="To start Application in your Project")
def startapp(name: str):
    create_folder(name)
    create_files(name, app_files)
    typer.secho(f"Created module {name} successfully 🎉🎉🎉", fg=typer.colors.GREEN)


# command to remove app
@app.command(help="Remove Application")
def remove(name: str):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), name))
        typer.echo(f"Removed successfully {name}")
    except FileNotFoundError:
        typer.echo("No such file or directory")


#allow to run fastapi server
@app.command(help="Run a FastAPI Server.")
def run(prod: bool = typer.Option(False)):
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
        if i==(len(files)-1):
            with open(f"./{name}/{list(files.keys())[i]}", 'w') as file:
                file.write(str(files[list(files.keys())[i]]).format(name))
        else:
            with open(f"./{name}/{list(files.keys())[i]}", 'w') as file:
                file.write(files[list(files.keys())[i]])




if __name__ == "__main__":
    app()
