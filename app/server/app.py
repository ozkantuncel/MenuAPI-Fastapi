from fastapi import FastAPI
from .routes.meal import router as MealRouter
from .routes.cart import router as CartRouter


app = FastAPI()

app.include_router(MealRouter, tags=["Meals"],prefix="/meals")
app.include_router(CartRouter, tags=["Carts"],prefix="/carts")




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}