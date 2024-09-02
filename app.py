from fastapi import FastAPI

from fireflies_wrapper import FirefliesWrapper

app = FastAPI()
fireflies = FirefliesWrapper()


@app.get("/")
async def root():
    return {"app": "fireflies.forgefx.tools", "version": "v2024.09.02-02"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/user_count")
async def get_user_count():
    count = fireflies.get_user_count()
    return {"user_count": count}
