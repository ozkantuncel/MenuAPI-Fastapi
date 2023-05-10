import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

databaseMeal = client["meals"]
databaseCart = client["carts"]

menu_collection = databaseMeal.get_collection("meals")
cart_collection = databaseCart.get_collection("carts")

def maeal_helper(menu)-> dict:
    return {
        "id":str(menu["_id"]),
        "yemek_id": int(menu["yemek_id"]),
        "yemek_adi": str(menu["yemek_adi"]),
        "yemek_resim_adi": str(menu["yemek_resim_adi"]),
        "yemek_fiyat": int(menu["yemek_fiyat"])
    }

def cart_helper(cart) ->dict:
    return {
        "sepet_yemek_id": str(cart["_id"]),
        "yemek_adi": str(cart["yemek_adi"]),
        "yemek_resim_adi": str(cart["yemek_resim_adi"]),
        "yemek_fiyat": int(cart["yemek_fiyat"]),
        "yemek_siparis_adet": int(cart["yemek_siparis_adet"]),
        "kullanici_adi": str(cart["kullanici_adi"])
    }


async def retrieve_meals():
    meal = []
    async for menu in menu_collection.find():
        meal.append(maeal_helper(menu))
    return meal


async def add_cart(cart_data:dict)-> dict:
    try:
        await cart_collection.insert_one(cart_data)
        return 1,"Cart added successfully."
    except:
        return 0,"Cart did not add."

async def retrieve_cart(kullanici_adi:str) ->dict:
    carts = []
    async for cart in cart_collection.find({"kullanici_adi": kullanici_adi}):
        carts.append(cart_helper(cart))
    return carts


async def delete_cart(id: str, kullanici_adi: str):
    try:
        student = await cart_collection.find_one({"_id": ObjectId(id), "kullanici_adi": kullanici_adi})
        if student:
            await cart_collection.delete_one({"_id": ObjectId(id), "kullanici_adi": kullanici_adi})
            return True
        return False
    except:
        return False
