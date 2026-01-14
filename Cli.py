import typer
app=typer.Typer()
@app.command()
def hello():
  print("welcome to Cz , press model to get a list of available models  ")
  print("enter select  (name of model) to activate that model")
  
@app.command()
def model():
  //research & add more models 
  print("Chatgpt")
  print("ClaudeAI")
  print("Gemini")
  print("NanoBanana")
  print("PicassoAI")
  print ("Deepseek")
  print("Copilot")
  print("MistralAI")
  print("MidJourney")
  print("DALLE3")
  print("StableDiffusion")
  
  
 @app.command():
def select(model_name:str):
  if model_name=="Chatgpt" :
    print("model selected , you can prompt now using Chatgt_prompt <your-prompt>")
  elif model_name=="ClaudeAI" :
    print("model selected , you can prompt now using ClaudeAI_prompt <your-prompt>")
  elif model_name=="Gemini":
    print("model selected , you can prompt now using Gemini_prompt <your-prompt>")
  elif model_name=="NanoBanana " :
    print("model selected , you can prompt now using NanoBanana_prompt <your-prompt>")
  elif model_name=="PicassoAI" :
    print("model selected, you can now prompt nusing PicassoAI_prompt <your-prompt>")
  elif model_name=="Deepseek":
    print("model selected , you can prompt now using Deepseek_prompt <your-prompt>")
  elif model_name=="Copilot":
    print("model selected , you can prompt now using Copilot_prompt <your-prompt>")
  elif model_name=="MistralAI":
    print("model selected , you can prompt now using MistralAI_prompt <your-prompt>")
  elif model_name=="MidJourney":
    print("model selected, you can prompt now using MidJourney_prompt <your-prompt>")
  elif model_name=="DALLE3":
    print("model selected, you can prompt now using DALLE3_prompt <your-prompt>")
  elif model_name=="StableDiffusion":
    print("model selected , you can prompt now using StableDiffusion_prompt<your-prompt>")



if __name__=="__main__":
  app()
  

