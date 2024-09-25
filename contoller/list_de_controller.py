from fastapi import APIRouter
from model import model
from service import list_de_service

listse_router = APIRouter(
  prefix="/listse"
)

listse_service = list_de_service.ListSEService()

@listse_router.get("/")
async def get_kids_list():
    return listse_service.get_kids().get_head()


@listse_router.post("/add")
async def add(data : model.Kid):
    listse_service.get_kids().add(data)
    return {"code": 200, "message": "creado"}

@listse_router.post("/tostart")
async def addToStart(data : model.Kid):
    listse_service.get_kids().addToStart(data)
    return {"code": 200, "message": "se agregó a la cabeza"}

@listse_router.post("/invert")
async def invert():
    result_message = listse_service.get_kids().invert()
    return {"code": 200, "message": result_message}

@listse_router.post("/addposition/{position}")
async def addInPosition(data: model.Kid, position: int):
    listse_service.get_kids().addInPosition(data, position)
    return {"code": 200, "message": "El nodo ha sido añadido en la posición"}

@listse_router.post("/deleteid/{id}")
async def deleteById(id: str):
    result_message = listse_service.get_kids().deleteById (id)
    return {"code": 200, "message": result_message}

@listse_router.post("/deletepos/{position}")
async def deleteByPosition(position: int):
    result_message = listse_service.get_kids().deleteByPosition(position)
    return {"code": 200, "message": result_message}

@listse_router.post("/tailHead")
async def changeExtremes():
    result_message = listse_service.get_kids().changeExtremes()
    return {"code": 200, "message": result_message}

@listse_router.post("/mixbygender")
async def mixByGender():
    result_message = listse_service.get_kids().mixByGender()
    return {"code": 200, "message": result_message}




