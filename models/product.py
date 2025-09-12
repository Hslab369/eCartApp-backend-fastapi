from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import Column, String, null

# CREATE TABLE product (
#   prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   image_path TEXT,
#   price REAL NOT NULL,
#   cat_id INTEGER NOT NULL,
#   is_popular INTEGER CHECK(is_popular IN (0,1)) DEFAULT 0,
#   FOREIGN KEY(cat_id) REFERENCES category(cat_id)
# );


class Product(SQLModel, table=True):
    prod_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    imgPath: Optional[str] = Field(
        default="", sa_column=Column("image_path", String, nullable=True)
    )
    price: Optional[float] = 0.0
    is_popular: Optional[bool] = False
    cat_id: int = Field(foreign_key="category.cat_id")
    category: "Category" = Relationship(back_populates="products")
