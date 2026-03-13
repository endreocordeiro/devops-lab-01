from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.get("/users")
def list_users():
    return {"users": []}