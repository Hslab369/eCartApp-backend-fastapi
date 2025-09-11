from typing import List
from sqlmodel import Field, Relationship, SQLModel

# CREATE TABLE category (
#   cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL
# );


class Category(SQLModel, table=True):
    cat_id: int = Field(default=None, primary_key=True)
    name: str = Field(default="", nullable=False)
    products: List["Product"] = Relationship(back_populates="category")
