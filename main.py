from math import prod
from fastapi import FastAPI, Depends
from typing import List, Optional
from config import setup_cors
from models import product
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


class ProductCreate(SQLModel):
    cat_id: int
    name: str
    price: float = 0.0
    imgPath: Optional[str] = None
    is_popular: bool = False


class CategoryReadWithId(SQLModel):
    cat_id: int
    name: str


class ProductReadWithId(SQLModel):
    prod_id: int
    name: str
    imgPath: str
    price: float
    category: CategoryReadWithId


# class ProductReadBatch(SQLModel):
#     name: str
#     imgPath: Optional[str] = None
#     price: float = 0.0
#     is_popular: bool = False


class ProductBatch(SQLModel):
    cat_id: int
    names: List[str]


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


@app.post("/addProduct", response_model=ProductReadWithId, tags=["Products"])
def add_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product.model_validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@app.get(
    "/getCategorieswithId", response_model=List[CategoryReadWithId], tags=["Categories"]
)
def list_categories_with_id(session: Session = Depends(get_session)):
    statement = select(Category)
    categories = session.exec(statement).all()
    return categories


@app.post("/addProductBatch", response_model=List[ProductReadWithId], tags=["Products"])
def add_product_batch(
    productsbatch: ProductBatch, session: Session = Depends(get_session)
):
    db_products = [
        Product(name=product_name, cat_id=productsbatch.cat_id)
        for product_name in productsbatch.names
    ]

    session.add_all(db_products)
    session.commit()
    for db_product in db_products:
        session.refresh(db_product)

    return db_products
