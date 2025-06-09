from pydantic import BaseModel
from typing import List

class MenuItem(BaseModel):
    id: int
    name: str
    price: float

class Hotel(BaseModel):
    id: int
    name: str
    menu: List[MenuItem]

class Order(BaseModel):
    client_id: int
    hotel_id: int
    items: List[int]

class Rating(BaseModel):
    client_id: int
    hotel_id: int
    rating: int
