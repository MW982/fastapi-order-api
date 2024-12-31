from fastapi import FastAPI

from orderapp import views as orderapp
from itemapp import views as itemapp

app = FastAPI()


app.include_router(orderapp.router)
app.include_router(itemapp.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


