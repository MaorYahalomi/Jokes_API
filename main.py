import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_punchline():
    resp = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke: dict = resp.json()
    return joke["id"], joke["punchline"]
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8877)