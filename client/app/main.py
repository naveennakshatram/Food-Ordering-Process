from fastapi import FastAPI
from app.models import OrderRequest, Rating
from app.services import fetch_hotels, place_order, submit_rating

app = FastAPI()

@app.get("/hotels")
async def get_hotels():
    return await fetch_hotels()

@app.post("/order")
async def order_food(order: OrderRequest):
    return await place_order(order.dict())

@app.post("/rating")
async def give_rating(rating: Rating):
    return await submit_rating(rating.dict())
