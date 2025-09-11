from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Float, String
from enum import Enum

# CREATE TABLE "order" (
#   ord_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   ord_date DATE NOT NULL,
#   amount REAL NOT NULL,
#   status TEXT CHECK(status IN ('pending', 'delivered', 'cancelled')) NOT NULL
# );


class OrderStatus(str, Enum):
    pending = "pending"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(SQLModel, table=True):
    ord_id: int = Field(default=None, primary_key=True)
    date: str = Field(default="", sa_column=Column("ord_date", String))
    price: float = Field(default=0.0, sa_column=Column("amount", Float))
    status: OrderStatus = Field(
        default=OrderStatus.pending, sa_column=Column("status", String)
    )
