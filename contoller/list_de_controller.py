from fastapi import APIRouter
from model import model
from service import list_de_service

listde_router = APIRouter(
  prefix="/listde"
)

list_de_service = list_de_service.ListDEService()

@listde_router.get("/")
async def get_kids_list():
    return list_de_service.get_kids().get_head()


@listde_router.post("/add")
async def add(data : model.Kid):
    list_de_service.get_kids().add(data)
    return {"code":200, "message": "creado"}