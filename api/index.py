from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "working"}

@app.get("/hello")
def hello():
    return {"message": "hello world"}