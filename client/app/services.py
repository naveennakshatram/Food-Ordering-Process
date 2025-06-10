import httpx

HOTEL_SERVICE_URL = "http://0.0.0.0:8002"
DELIVERY_SERVICE_URL = "http://0.0.0.0:8003"

async def fetch_hotels():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HOTEL_SERVICE_URL}/hotels")
        return response.json()

async def place_order(data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{HOTEL_SERVICE_URL}/orders", json=data)
        return response.json()

async def submit_rating(data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{HOTEL_SERVICE_URL}/ratings", json=data)
        return response.json()
