from typing import Optional

from pydantic import BaseModel, Field

class CartSchema(BaseModel):
    yemek_adi: str 
    yemek_resim_adi: str 
    yemek_fiyat: int
    yemek_siparis_adet:int 
    kullanici_adi:str

def ResponseModel(data, success):
    return {
        "yemekler":data,
        "success": success
    }

def ResponseModelCart(data, success):
    return {
        "sepet_yemekler": data,
        "success": success
    }

def ResponseModelCartR(success,message):
    return {
        "success": success,
        "message": message,
    }
    

def ErrorResponseModel(success, message):
    return {
             "success": success, 
             "message": message
    }
