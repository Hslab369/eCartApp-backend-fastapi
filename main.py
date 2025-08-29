from fastapi import FastAPI
from typing import List
from config import setup_cors
from models.product import Product
from models.category import Category
from models.order import Order

app = FastAPI()

setup_cors(app)

# ----------------
# Inline Data
# ----------------
getFrequentlyOrdered = [
    Product(name="iPhone 15", imgPath="iphone.jpg", price=999),
    Product(name="MacBook Pro", imgPath="macbook.jpg", price=1999),
    Product(name="AirPods Pro", imgPath="airpods.jpg", price=249),
]

getCategories = [
    Category(
        name="Mobiles",
        products=[
            Product(name="Samsung Galaxy S24", imgPath="samsung.jpg", price=899),
            Product(name="Google Pixel 9", imgPath="pixel.jpg", price=799),
            Product(name="iPhone 15", imgPath="iphone.jpg", price=999),
        ],
    ),
    Category(
        name="Laptops",
        products=[
            Product(name="Dell XPS 15", imgPath="dell.jpg", price=1500),
            Product(name="Lenovo ThinkPad", imgPath="thinkpad.jpg", price=1200),
            Product(name="MacBook Pro", imgPath="macbook.jpg", price=1999),
        ],
    ),
    Category(
        name="Accessories",
        products=[
            Product(name="AirPods Pro", imgPath="airpods.jpg", price=249),
            Product(name="Apple Watch Series 8", imgPath="watch.jpg", price=399),
        ],
    ),
]

getProducts = [
    Product(name="Mouse", price=1299, imgPath="mouse.jpeg"),
    Product(name="Keyboard", price=3000, imgPath="keyboard.jpeg"),
    Product(name="Monitor", price=11000, imgPath="monitor.jpeg"),
    Product(name="Speaker", price=10000, imgPath="speaker.jpeg"),
    Product(name="Webcam", price=1599, imgPath="webcam.jpeg"),
    Product(name="Laptop", price=75000, imgPath="laptop.jpeg"),
    Product(name="Tablet", price=50000, imgPath="tablet.jpeg"),
    Product(name="T-Shirt", price=1599, imgPath="tshirt.jpeg"),
    Product(name="Shirt", price=1000, imgPath="shirt.jpeg"),
    Product(name="Bag", price=1599, imgPath="bag.jpeg"),
    Product(name="Travel Bag", price=2299, imgPath="travelbag.jpeg"),
    Product(name="Mobile", price=1500, imgPath="mobile.jpeg"),
    Product(name="Table", price=11000, imgPath="table.jpeg"),
    Product(name="Cupboard", price=12999, imgPath="cubboard.jpeg"),
    Product(name="Watch", price=2000, imgPath="watch.jpg"),
    Product(name="HeadPhone", price=1599, imgPath="headphones.jpeg"),
]

getOrders = [
    Order(date="2025-08-22", price=1299, status="Delivered"),
    Order(date="2025-08-20", price=499, status="Pending"),
    Order(date="2025-08-18", price=899, status="Cancelled"),
]


# ----------------
# Routes
# ----------------
@app.get("/")
def root():
    return {"Hello": "World!", "Server Status": "Active"}


@app.get("/getFrequentlyOrdered", response_model=List[Product])
def list_frequently_ordered():
    return getFrequentlyOrdered


@app.get("/getCategories", response_model=List[Category])
def list_categories():
    return getCategories


@app.get("/getProducts", response_model=List[Product])
def list_products():
    return getProducts


@app.get("/getOrders", response_model=List[Order])
def list_orders():
    return getOrders
