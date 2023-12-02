from fastapi import APIRouter

api = APIRouter()

@api.get("/")
async def test():
    return {"message": "hola"}