from pydantic import BaseModel
from typing import List

"""
    ✅ What Is BaseModel ?
        BaseModel is a class from Pydantic that lets you define a data schema with validation. 
        It ensures that data coming in (like JSON from a POST request) has the correct fields and types.
    
    ✅ What Is List ?
        List is part of Python's type hinting system, and it comes from the built-in typing module. 
        It allows you to specify that a variable, function parameter, or return value should be a list of a specific type.
"""

class MenuItem(BaseModel):
    id: int
    name: str
    price: float

class Hotel(BaseModel):
    id: int
    name: str
    menu: List[MenuItem]

class OrderRequest(BaseModel):
    client_id: int
    hotel_id: int
    items: List[int]  # Menu item IDs

class Rating(BaseModel):
    client_id: int
    hotel_id: int
    rating: int  # 1 to 5
