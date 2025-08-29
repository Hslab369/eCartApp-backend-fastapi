from pydantic import BaseModel

class Order(BaseModel):
    date: str
    price: float
    status: str