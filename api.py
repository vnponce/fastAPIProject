from fastapi import APIRouter, status

api = APIRouter()


@api.get("/", status_code=status.HTTP_200_OK)
async def test():
    return {"no": "hola"}
