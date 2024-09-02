from fastapi import FastAPI, HTTPException
from fireflies_wrapper import FirefliesWrapper

app = FastAPI()

try:
    fireflies = FirefliesWrapper()
except ValueError as e:
    print(f"Error initializing FirefliesWrapper: {e}")
    fireflies = None

@app.get("/")
async def root():
    return {"app": "fireflies.forgefx.tools", "version": "v2024.09.02-02"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/user_count")
async def get_user_count():
    if fireflies is None:
        raise HTTPException(status_code=500, detail="FirefliesWrapper not initialized")
    count = fireflies.get_user_count()
    return {"user_count": count}
