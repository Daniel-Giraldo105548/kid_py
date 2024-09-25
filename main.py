from fastapi import FastAPI
from contoller import list_de_controller
from contoller import list_de_controller_DE

app = FastAPI()

app.include_router(list_de_controller.listse_router)
app.include_router(list_de_controller_DE.listde_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

