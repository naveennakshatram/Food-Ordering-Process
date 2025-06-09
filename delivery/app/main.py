from fastapi import FastAPI
from app.models import Order
from app.delivery_data import delivery_boys, deliveries
import random

app = FastAPI()

@app.post("/dispatch")
def dispatch_order(order: Order):
    delivery_boy = random.choice(delivery_boys)
    order_id = f"{order.client_id}-{order.hotel_id}"

    deliveries[order_id] = {
        "status": "Out for delivery",
        "delivery_boy": delivery_boy
    }

    return {
        "order_id": order_id,
        "status": "Dispatched",
        "delivery_boy": delivery_boy
    }

@app.get("/delivery-status/{order_id}")
def get_status(order_id: str):
    delivery = deliveries.get(order_id)
    if not delivery:
        return {"status": "Not Found"}

    return {
        "order_id": order_id,
        "status": delivery["status"],
        "delivery_boy": delivery["delivery_boy"]
    }

@app.post("/mark-delivered/{order_id}")
def mark_delivered(order_id: str):
    if order_id in deliveries:
        deliveries[order_id]["status"] = "Delivered"
        return {"message": "Order marked as delivered"}
    return {"message": "Order not found"}
