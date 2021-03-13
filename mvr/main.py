import os
import typer

app = typer.Typer()

@app.command()
def init(name: str):
    os.mkdir(os.path.join(os.getcwd(),name))
    typer.echo(f"Created project {name} successfully.\ncd {name}")

@app.command()
def startapp(name: str):
    typer.echo(f"Created module {name} successfully")


if __name__ =="__main__" :
    app()