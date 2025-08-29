# 🛠️ E-commerce API (FastAPI)
A simple **e-commerce backend** built with **FastAPI**.  
Provides product, category, order, and frequently ordered data to an Angular frontend.

***

## 🚀 Features
- [x] **Basic REST API** with FastAPI
- [x] **CORS support** (development, all origins allowed)   
- [ ] **Typed responses using Pydantic models** _(planned)_  
- [ ] **Modular routes** for products, categories, and orders _(planned)_  
- [ ] **Service layer separation** _(planned)_  
- [ ] **SQLite / Postgres database integration** _(planned)_  
- [ ] **Authentication (JWT)** _(planned)_  
- [ ] **Unit & integration tests** _(planned)_

***

## 📂 Project Structure (Initial)
```
backend/
│
├── app/
│   ├── main.py            # Application entry point
│   ├── config.py          # Settings (planned)
│   ├── models/            # Pydantic models (planned)
│   ├── routes/            # API routes (planned)
│   ├── services/          # Business logic (planned)
│   └── tests/             # Unit tests (planned)
│
├── Pipfile
├── Pipfile.lock
└── README.md
```


***

## ⚙️ Setup & Installation

1. **Clone repository**
    ```bash
    git clone https://github.com/Hslab369/eCartApp-backend-fastapi.git
    cd eCartApp-backend-fastapi
    ```
2. **Install pipenv (if needed)**
    ```bash
    pip install --user pipenv
    ```
3. **Install dependencies and create virtual environment**
    ```bash
    pipenv install
    ```
4. **Activate the pipenv shell**
    ```bash
    pipenv shell
    ```
5. **Run server**
    ```bash
    uvicorn app.main:app --reload
    ```


***

## 🌐 API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

***

## 🔗 API Endpoints (Initial)
| Endpoint                | Method | Description              |
|-------------------------|--------|--------------------------|
| `/getProducts`          | GET    | Get all products         |
| `/getCategories`        | GET    | Get all categories       |
| `/getOrders`            | GET    | Get all orders           |
| `/getFrequentlyOrdered` | GET    | Get frequently ordered   |

***
