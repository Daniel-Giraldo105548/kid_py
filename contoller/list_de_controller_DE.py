from fastapi import APIRouter
from model import model
from service import list_de_service_DE

listde_router = APIRouter(
  prefix="/listde"
)

listde_service = list_de_service_DE.ListDEService()

@listde_router.get("/")
async def show_kids():
    return listde_service.show_kids()

@listde_router.post("/add")
async def add(data: model.Kid):
    listde_service.get_kids().addDE(data)
    return {"code": 200, "message": "creado"}

@listde_router.post("/tostart")
async def addtostart(data: model.Kid):
    listde_service.get_kids().addToStart(data)
    return {"code": 200, "message": "agregado a la cabeza"}

@listde_router.post("/addposition/{position}")
async def addInPosition(data: model.Kid, position: int):
    listde_service.get_kids().addInPosition(data, position)
    return {"code": 200, "message": "El nodo ha sido añadido en la posición"}

@listde_router.post("/deleteposition/{position}")
async def deleteposition(position: int):
    listde_service.get_kids().deleteByPosition(position)
    return {"code": 200, "message": "El nodo ha sido eliminado"}
@listde_router.post("/deleteid/{id}")
async def deleteid(id: int):
    return listde_service.get_kids().deleteById(id)
@listde_router.post("/invert")
async def invert():
    listde_service.get_kids().invert()
    return {"code": 200, "message": "El nodo se invertio"}

@listde_router.post("/changeextremes")
async def changeextremes():
    return listde_service.get_kids().changeExtremes()