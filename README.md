# 🛠️ E-commerce API (FastAPI)

A simple **e-commerce backend** built with **FastAPI**.  
This project powers the Angular frontend 👉 [eCartApp](https://github.com/Hslab369/eCartApp) by providing **products, categories, orders, and frequently ordered items**.

---

## 🚀 Features

- [x] **FastAPI REST API** with auto-generated docs
- [x] **CORS enabled** for frontend integration
- [x] **JSON responses** for products, categories, and orders
- [x] **Pydantic models** for typed responses
- [x] **SQLite database integration** using SQLModel
- [ ] **Modular routes** (`products`, `categories`, `orders`) 🚧 Planned
- [ ] **Postgres database integration** 🚧 Planned
- [ ] **Authentication (JWT)** 🚧 Planned
- [ ] **Unit & integration tests** 🚧 Planned

---

## 📂 Project Structure (Current)

```
├── main.py            # Application entry point
├── config.py          # Settings
├── db.py              # Database connection
├── models/            # Pydantic models
│   ├── category.py
│   ├── order.py
│   ├── product.py
├── eCartApp.db        # SQLite database file
├── Pipfile            # Pipenv dependency management
├── Pipfile.lock       # Pipenv dependency lock
└── README.md          # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hslab369/eCartApp-backend-fastapi.git
   cd eCartApp-backend-fastapi
   ```

2. **Install dependencies**

   Make sure you have **pipenv** installed:

   ```bash
   pip install --user pipenv
   ```

   Then install project dependencies:

   ```bash
   pipenv install
   ```

3. **Activate the pipenv shell**

   ```bash
   pipenv shell
   ```

4. **Run the development server**

   ```bash
   uvicorn app.main:app --reload
   ```

Server will be available at: **http://127.0.0.1:8000**

---

## 🌐 API Documentation
<img width="960" height="540" alt="Swagger UI docs" src="https://github.com/user-attachments/assets/9529180d-d699-40fa-82b6-c94901ef0a6b" />

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔗 API Endpoints (Current)

| Endpoint                | Method | Description            | Example Response                                               |
| :---------------------- | :----- | :--------------------- | :------------------------------------------------------------- |
| `/getProducts`          | GET    | Get all products       | `[{"id":1,"name":"Product A","price":120,"imgPath":"p1.png"}]` |
| `/getCategories`        | GET    | Get all categories     | `[{"id":1,"name":"Electronics","products":[...]}]`             |
| `/getOrders`            | GET    | Get all orders         | `[{"id":101,"user":"John","items":[...]}]`                     |
| `/getFrequentlyOrdered` | GET    | Get frequently ordered | `[{"id":2,"name":"Product B","price":90,"imgPath":"p2.png"}]`  |

---

## 🤝 Contribution
This project is for learning/demo purposes, but PRs are welcome
1. **Fork** the repo
2. Create a new feature branch

   ```bash
   git checkout -b feature-name
   ```

3. Commit changes

   ```bash
   git commit -m "Add feature"
   ```

4. Push branch

   ```bash
   git push origin feature-name
   ```

5. Open a **Pull Request**

---

## 💡 Tip

Run this backend **together with the Angular frontend** [eCartApp](https://github.com/Hslab369/eCartApp) to see the **full stack in action**! 🚀


<img width="1920" height="1080" alt="Angular frontend consuming API" src="https://github.com/user-attachments/assets/0b61687b-3ab6-4111-9dc3-b0e912f27c0e" />
<img width="1920" height="1080" alt="Angular frontend consuming API" src="https://github.com/user-attachments/assets/d5c95f00-d55b-49f3-98b9-99e11f330661" />
