import requests
import httpx

DELIVERY_SERVICE_URL = "http://0.0.0.0:8003"

async def notify_delivery(order_data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{DELIVERY_SERVICE_URL}/deliver", json=order_data)
        print("Delivery service response status:", response.status_code)
        print("Delivery service response text:", response.text)
        response.raise_for_status()
        return response.json()


