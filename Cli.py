import typer
app=typer.Typer()
@app.command()
def hello(name:str):
  print(f"welcome! {name}")
@app.command()
def goodbye(name_x:str):
  print( f"goodbye{name_x}")
if __name__=="__main__":
  app()
  

