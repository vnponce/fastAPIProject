from pydantic import BaseModel
from typing import Optional


class ResponseSchema(BaseModel):
    message: str


class CategorySchema(BaseModel):
    id: Optional[int]
    name: str
    slug: Optional[str]

    class Config:
        schema_extra = {
            "test": {
                "name": "test name"
            }
        }


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    price: int
    categories_id: int

    class Config:
        schema_extra = {
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
