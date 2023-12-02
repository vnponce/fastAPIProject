from pydantic import BaseModel
from typing import Optional


class ResponseSchema(BaseModel):
    message: str


class BaseCategorySchema(BaseModel):
    name: str



class CategorySchemaOut(BaseCategorySchema):
    id: int
    slug: str


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    price: int
    categories_id: int

    class Config:
        json_schema_extra = {
            "test": {
                "name": "test product name",
                "description": "test product description",
                "price": 1,
                "categories_id": 1,
            }
        }


class ProductPhotoSchema(BaseModel):
    id: Optional[int]
    name: str
    products_id: int
