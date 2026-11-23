from fastapi import FastAPI

from .router import uploader

app = FastAPI()

app.include_router(uploader.router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
