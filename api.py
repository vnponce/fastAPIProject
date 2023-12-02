from typing import List

from fastapi import APIRouter, status, HTTPException
from database import connect
from schemas import *
from models import *

api = APIRouter()


@api.get("/categories", response_model=List[CategorySchema])
async def categories():
    return connect.execute(categories_model.select()).fetchall()
