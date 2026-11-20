from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Server working"}