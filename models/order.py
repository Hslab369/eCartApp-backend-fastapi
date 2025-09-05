from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Float, String


class Order(SQLModel, table=True):
    ord_id: int = Field(default=None, primary_key=True)
    date: str = Field(sa_column=Column("ord_date", String))
    price: float = Field(sa_column=Column("amount", Float))
    status: str
