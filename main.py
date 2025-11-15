from fastapi import FastAPI

app = FastAPI()

app.get("/")
async def homepage():
    return{"message":"Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}