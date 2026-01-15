import typer
import os

app = typer.Typer()

# Fetch API keys
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
CLAUDEAI_KEY = os.getenv("CLAUDEAI_API_KEY")
NANOBANANA_KEY = os.getenv("NANOBANANA_API_KEY")
PICASSOAI_KEY = os.getenv("PICASSOAI_API_KEY")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")
COPILOT_KEY = os.getenv("COPILOT_API_KEY")
MISTRALAI_KEY = os.getenv("MISTRALAI_API_KEY")
MIDJOURNEY_KEY = os.getenv("MIDJOURNEY_API_KEY")
DALLE3_KEY = os.getenv("DALLE3_API_KEY")
STABLEDIFFUSION_KEY = os.getenv("STABLEDIFFUSION_API_KEY")

# Error handling to check if keys are missing
keys = {
    "OPENAI_KEY": OPENAI_KEY,
    "CLAUDEAI_KEY": CLAUDEAI_KEY,
    "NANOBANANA_KEY": NANOBANANA_KEY,
    "PICASSOAI_KEY": PICASSOAI_KEY,
    "DEEPSEEK_KEY": DEEPSEEK_KEY,
    "COPILOT_KEY": COPILOT_KEY,
    "MISTRALAI_KEY": MISTRALAI_KEY,
    "MIDJOURNEY_KEY": MIDJOURNEY_KEY,
    "DALLE3_KEY": DALLE3_KEY,
    "STABLEDIFFUSION_KEY": STABLEDIFFUSION_KEY,
}

for key_name, key_value in keys.items():
    if not key_value:
        raise ValueError(f"{key_name} is missing. Please check again.")

@app.command()
def hello():
    typer.echo("Welcome to Cz, press 'model' to get a list of available models")
    typer.echo("Enter 'select <name of model>' to activate that model")
    typer.echo("Enter 'help_commands' to display list of commands")

@app.command()
def model():
    # Research & add more models
    models = [
        "Chatgpt", "ClaudeAI", "Gemini", "NanoBanana", "PicassoAI",
        "Deepseek", "Copilot", "MistralAI", "MidJourney", "DALLE3", "StableDiffusion"
    ]
    for m in models:
        typer.echo(m)

@app.command()
def select(model_name: str):
    if model_name == "Chatgpt":
        typer.echo("Model selected. Use Chatgpt_prompt <your-prompt>")
    elif model_name == "ClaudeAI":
        typer.echo("Model selected. Use ClaudeAI_prompt <your-prompt>")
    elif model_name == "Gemini":
        typer.echo("Model selected. Use Gemini_prompt <your-prompt>")
    elif model_name == "NanoBanana":
        typer.echo("Model selected. Use NanoBanana_prompt <your-prompt>")
    elif model_name == "PicassoAI":
        typer.echo("Model selected. Use PicassoAI_prompt <your-prompt>")
    elif model_name == "Deepseek":
        typer.echo("Model selected. Use Deepseek_prompt <your-prompt>")
    elif model_name == "Copilot":
        typer.echo("Model selected. Use Copilot_prompt <your-prompt>")
    elif model_name == "MistralAI":
        typer.echo("Model selected. Use MistralAI_prompt <your-prompt>")
    elif model_name == "MidJourney":
        typer.echo("Model selected. Use MidJourney_prompt <your-prompt>")
    elif model_name == "DALLE3":
        typer.echo("Model selected. Use DALLE3_prompt <your-prompt>")
    elif model_name == "StableDiffusion":
        typer.echo("Model selected. Use StableDiffusion_prompt <your-prompt>")

@app.command()
def help_commands():
    typer.echo("select -- select <model name> is used to activate an AI model")
    typer.echo("modelname_prompt -- prompt to the selected model")
    typer.echo("help_commands -- lists all help commands")
    typer.echo("models -- lists all existing models")

@app.command()
def models():
    model_list = [
        "Chatgpt", "ClaudeAI", "Gemini", "NanoBanana", "PicassoAI",
        "Deepseek", "Copilot", "MistralAI", "MidJourney", "DALLE3", "StableDiffusion"
    ]
    for m in model_list:
        typer.echo(m)

if __name__ == "__main__":
    app()

  

