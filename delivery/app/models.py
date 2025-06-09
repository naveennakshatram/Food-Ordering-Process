from pydantic import BaseModel
from typing import List

class Order(BaseModel):
    client_id: int
    hotel_id: int
    items: List[int]
