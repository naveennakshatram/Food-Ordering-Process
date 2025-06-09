from fastapi import FastAPI, HTTPException
from app.models import Order, Rating
from app.hotels_data import hotels
from app.services import notify_delivery

app = FastAPI()

@app.get("/hotels")
def get_all_hotels():
    return list(hotels.values())

@app.post("/orders")
async def place_order(order: Order):
    hotel = hotels.get(order.hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    # Optionally process or store the order
    dispatch_response = await notify_delivery(order.dict())
    return {"status": "Order accepted", "delivery": dispatch_response}

@app.post("/ratings")
def rate_hotel(rating: Rating):
    hotel = hotels.get(rating.hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    hotel["ratings"].append(rating.rating)
    return {"message": "Rating submitted", "average_rating": sum(hotel["ratings"]) / len(hotel["ratings"])}
