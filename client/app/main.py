from fastapi import FastAPI
from models import OrderRequest, Rating
import services

app = FastAPI()

@app.get("/hotels")
async def get_hotels():
    return await services.fetch_hotels()

@app.post("/order")
async def order_food(order: OrderRequest):
    return await services.place_order(order.dict())

@app.post("/rating")
async def give_rating(rating: Rating):
    return await services.submit_rating(rating.dict())
