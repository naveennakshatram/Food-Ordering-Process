import requests

DELIVERY_SERVICE_URL = "http://delivery:5002"

def notify_delivery(order_data):
    try:
        res = requests.post(f"{DELIVERY_SERVICE_URL}/deliver", json=order_data)
        return res.json()
    except Exception as e:
        return {"error": str(e)}
