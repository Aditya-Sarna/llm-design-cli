import typer
app=typer.Typer()
@app.command()
def hello():
  print("welcome to Cz , press model to get a list of available models  ")
  print("enter model (name of model) to activate that model")
@app.command()
def model():
  print("Chatgpt")
  print("ClaudeAI")
  print("Gemini")
  print("Nano Banana")
  print("Picasso ai")
  print ("deepseek")
  print("copilot")
  
  
 
if __name__=="__main__":
  app()
  

