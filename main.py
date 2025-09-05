from fastapi import FastAPI, Depends
from typing import List
from config import setup_cors
from models.product import Product
from models.category import Category
from models.order import Order
from db import get_session
from sqlmodel import SQLModel, Session, select


# ----------------
# Pydantic Models for Response Schemas (Restricting Data)
# ----------------
class OrderRead(SQLModel):
    date: str
    price: float
    status: str


class ProductRead(SQLModel):
    name: str
    imgPath: str
    price: float


class CategoryRead(SQLModel):
    name: str
    products: List[ProductRead] = []


app = FastAPI()

setup_cors(app)


# ----------------
# Routes
# ----------------
@app.get("/")
def root():
    return {"Hello": "World!", "Server Status": "Active"}


@app.get("/getFrequentlyOrdered", response_model=List[ProductRead], tags=["Orders"])
def list_frequently_ordered(session: Session = Depends(get_session)):
    return session.exec(select(Product).where(Product.is_popular == True)).all()


@app.get("/getCategories", response_model=List[CategoryRead], tags=["Categories"])
def list_categories(session: Session = Depends(get_session)):
    statement = select(Category)
    categories = session.exec(statement).all()
    return categories


@app.get("/getProducts", response_model=List[ProductRead], tags=["Products"])
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()


@app.get("/getOrders", response_model=List[OrderRead], tags=["Orders"])
def list_orders(session: Session = Depends(get_session)):
    return session.exec(select(Order)).all()
