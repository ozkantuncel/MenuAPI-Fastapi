from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_meals
)
from server.models.menu import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()


@router.get("/", response_description="Meals retrieved")
async def get_meals():
    meals = await retrieve_meals()
    if meals:
        return ResponseModel(meals,1)
    return ResponseModel(meals,0)