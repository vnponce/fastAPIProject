from typing import List
from slugify import slugify
from fastapi import APIRouter, status, HTTPException
from database import connect
from schemas import *
from models import *

api = APIRouter()


@api.get("/categories", response_model=List[CategorySchemaOut])
async def categories():
    return connect.execute(categories_model.select()).fetchall()


@api.get("/categories/{id}", response_model=CategorySchemaOut)
async def get_category(id: int):
    data = connect.execute(categories_model.select().where(categories_model.c.id == id)).first()
    if data:
        return data
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not found")


@api.post("/categories", response_model=ResponseSchema, status_code=status.HTTP_201_CREATED)
def create_category(category: BaseCategorySchema):
    print(category)
    try:
        connect.execute(
            categories_model.insert().values({"name": category.name, "slug": slugify(category.name)}))
        return {"message": "crreated"}
    except ValueError:
        print(ValueError)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
