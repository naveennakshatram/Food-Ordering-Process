import httpx

HOTEL_SERVICE_URL = "http://hotel:5001"
DELIVERY_SERVICE_URL = "http://delivery:5002"

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
