from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

getFrequentlyOrdered = [
    {"name": "iPhone 15", "imgPath": "iphone.jpg", "price": 999},
    {"name": "MacBook Pro", "imgPath": "macbook.jpg", "price": 1999},
    {"name": "AirPods Pro", "imgPath": "airpods.jpg", "price": 249},
]

getCategories = [
    {
        "name": "Mobiles",
        "products": [
            {
                "name": "Samsung Galaxy S24",
                "imgPath": "samsung.jpg",
                "price": 899,
            },
            {
                "name": "Google Pixel 9",
                "imgPath": "pixel.jpg",
                "price": 799,
            },
            {"name": "iPhone 15", "imgPath": "iphone.jpg", "price": 999},
        ],
    },
    {
        "name": "Laptops",
        "products": [
            {"name": "Dell XPS 15", "imgPath": "dell.jpg", "price": 1500},
            {
                "name": "Lenovo ThinkPad",
                "imgPath": "thinkpad.jpg",
                "price": 1200,
            },
            {"name": "MacBook Pro", "imgPath": "macbook.jpg", "price": 1999},
        ],
    },
    {
        "name": "Accessories",
        "products": [
            {"name": "AirPods Pro", "imgPath": "airpods.jpg", "price": 249},
            {"name": "Apple Watch Series 8", "imgPath": "watch.jpg", "price": 399},
        ],
    },
]

getProducts = [
    {"name": "Mouse", "price": 1299, "imgPath": "mouse.jpeg"},
    {"name": "Keyboard", "price": 3000, "imgPath": "keyboard.jpeg"},
    {"name": "Monitor", "price": 11000, "imgPath": "monitor.jpeg"},
    {"name": "Speaker", "price": 10000, "imgPath": "speaker.jpeg"},
    {"name": "Webcam", "price": 1599, "imgPath": "webcam.jpeg"},
    {"name": "Laptop", "price": 75000, "imgPath": "laptop.jpeg"},
    {"name": "Tablet", "price": 50000, "imgPath": "tablet.jpeg"},
    {"name": "T-Shirt", "price": 1599, "imgPath": "tshirt.jpeg"},
    {"name": "Shirt", "price": 1000, "imgPath": "shirt.jpeg"},
    {"name": "Bag", "price": 1599, "imgPath": "bag.jpeg"},
    {"name": "Travel Bag", "price": 2299, "imgPath": "travelbag.jpeg"},
    {"name": "Mobile", "price": 1500, "imgPath": "mobile.jpeg"},
    {"name": "Table", "price": 11000, "imgPath": "table.jpeg"},
    {"name": "Cupboard", "price": 12999, "imgPath": "cubboard.jpeg"},
    {"name": "Watch", "price": 2000, "imgPath": "watch.jpg"},
    {"name": "HeadPhone", "price": 1599, "imgPath": "headphones.jpeg"},
]

getOrders = [
    {"date": "2025-08-22", "price": 1299, "status": "Delivered"},
    {"date": "2025-08-20", "price": 499, "status": "Pending"},
    {"date": "2025-08-18", "price": 899, "status": "Cancelled"},
]


@app.get("/")
def root():
    return {"Hello": "World!"}, {"Server Status": "Active"}


@app.get("/getFrequentlyOrdered")
def list_frequently_ordered():
    return getFrequentlyOrdered


@app.get("/getCategories")
def list_categories():
    return getCategories


@app.get("/getProducts")
def list_products():
    return getProducts


@app.get("/getOrders")
def list_orders():
    return getOrders
