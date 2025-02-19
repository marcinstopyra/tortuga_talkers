from fastapi import FastAPI
import logging
from openai import OpenAI
from tortuga_talkers.src.helpers.config_helper import load_config
from dotenv import load_dotenv
from tortuga_talkers.src.models.api import SimpleMessage
import os

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger(__name__)
config = load_config("./config.yml")

app = FastAPI()

@app.get("/")
def read_root():
    log.error("returning hello world")
    return {"message": "Hello, FastAPI!"}

@app.post("/test_api")
def test_api(message: SimpleMessage):

    client = OpenAI(
    api_key=OPENAI_API_KEY 
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "developer", "content": f"The model should answer to users message in {message.answer_language} language"},
        {"role": "user", "content": message.msg}
    ]
    )

    log.error(completion.choices[0].message)
    return {"msg": completion.choices[0].message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



