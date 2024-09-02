
from fastapi import FastAPI



from fireflies_wrapper import FirefliesWrapper

app = FastAPI()
fireflies = FirefliesWrapper()



@app.get("/")
async def root():
    return {"app": "fireflies.forgefx.tools v2024.09.02-01"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
