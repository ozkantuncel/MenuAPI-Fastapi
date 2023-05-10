from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_cart,
    retrieve_cart,
    delete_cart
)
from server.models.menu import (
    ErrorResponseModel,
    ResponseModelCart,
    ResponseModelCartR,
    CartSchema
)

router = APIRouter()

@router.get("/", response_description="Cart data retrieved")
async def get_cart_data(kullanici_adi:str):
    cart = await retrieve_cart(kullanici_adi)
    if cart:
        return ResponseModelCart(cart, 1)
    return ResponseModelCart([],0)


@router.post("/add", response_description="Cart data added into the database")
async def add_cart_data(cart: CartSchema = Body(...)):
    cart = jsonable_encoder(cart)
    s,m = await add_cart(cart)
    return ResponseModelCartR(s, m)


@router.delete("/delete", response_description="Cart data deleted from the database")
async def delete_cart_data(sepet_yemek_id: str, kullanici_adi: str):
    deleted_cart = await delete_cart(sepet_yemek_id, kullanici_adi)
    if deleted_cart:
        return ResponseModelCartR(
            1,f"{kullanici_adi} was delleted"
        )
    return ErrorResponseModel(
        0,f"{kullanici_adi} wasnt delleted"
    )


