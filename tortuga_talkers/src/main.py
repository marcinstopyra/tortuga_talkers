from fastapi import FastAPI
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    log.error("returning hello world")
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)