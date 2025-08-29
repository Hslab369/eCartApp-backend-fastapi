from pydantic import BaseModel
from typing import List
from .product import Product

class Category(BaseModel):
    name: str
    products: List[Product]