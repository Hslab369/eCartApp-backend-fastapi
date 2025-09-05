from typing import List
from sqlmodel import Field, Relationship, SQLModel


class Category(SQLModel, table=True):
    cat_id: int = Field(default=None, primary_key=True)
    name: str
    products: List["Product"] = Relationship(back_populates="category")
