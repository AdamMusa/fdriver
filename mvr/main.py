import os
import typer

app = typer.Typer()
files = ["models.py","views.py","routes.py","database.py"]
@app.command()
def init(name: str):
    os.mkdir(os.path.join(os.getcwd(),name))
    os.mkdir(os.path.join(os.getcwd(),name+"/fastapi"))
    with open(f"./{name}/fastapi/__init__.py",'w') as file:
        pass
    for file_name in files:
        with open(f"./{name}/{file_name}",'w') as file:
            for i in range(len(files)+1):
                file.write("print('hello world')")
                break
    
    typer.echo(f"Created project {name} successfully.\ncd {name}")

@app.command()
def startapp(name: str):
    typer.echo(f"Created module {name} successfully")


if __name__ =="__main__" :
    app()