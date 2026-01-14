import Typer
app=Typer.typer()
@app.command 
def hello(name:string):
  print(f"welcome! {name})
if __name__="__main__"
        app()
