# 🍽️ Foodie App REST API Testing Project

This project is a complete **Food Ordering REST API System** developed using **Flask** and tested using:

- ✅ Postman (Manual API Testing)
- ✅ Pytest (Automation Testing)
- ✅ Robot Framework (Keyword Driven Automation)

It contains 18 REST APIs covering Restaurant, Dish, User, Order, Rating, and Admin modules.

---

## 📌 Project Objective

The main objective of this project is to:

- Build a simple Food Ordering REST API backend using Flask
- Perform complete API testing using Postman
- Automate API testing using Pytest and Robot Framework
- Demonstrate end-to-end API validation without using any database

---

## 🚀 Tech Stack Used

| Technology | Purpose |
|----------|---------|
| Python | Backend Development |
| Flask | REST API Framework |
| Postman | Manual API Testing |
| Pytest | Automation Testing Framework |
| Robot Framework | Keyword Driven Testing |
| RequestsLibrary | Robot API Requests |
| In-Memory Storage | Data Handling (No DB) |

---

## 📂 Project Modules

This project contains the following modules:

### ✅ Restaurant Module
- Register Restaurant
- Update Restaurant
- Disable Restaurant
- View Restaurant Profile

### ✅ Dish Module
- Add Dish
- Update Dish
- Enable/Disable Dish
- Delete Dish

### ✅ Admin Module
- Approve Restaurant
- Disable Restaurant (Admin)
- View Feedback
- View All Orders

### ✅ User Module
- User Registration
- Search Restaurants
- Place Order
- Give Rating

### ✅ Order Module
- View Orders by Restaurant
- View Orders by User

---

## 📌 API Endpoints Summary (Module Wise)

---

### ✅ Restaurant Module APIs (1–4)

| API No | Method | Endpoint |
|-------|--------|----------|
| 1 | POST | `/api/v1/restaurants` |
| 2 | PUT  | `/api/v1/restaurants/1` |
| 3 | PUT  | `/api/v1/restaurants/1/disable` |
| 4 | GET  | `/api/v1/restaurants/1` |

---

### ✅ Dish Module APIs (5–8)

| API No | Method | Endpoint |
|-------|--------|----------|
| 5 | POST   | `/api/v1/restaurants/1/dishes` |
| 6 | PUT    | `/api/v1/dishes/1` |
| 7 | PUT    | `/api/v1/dishes/1/status` |
| 8 | DELETE | `/api/v1/dishes/1` |

---

### ✅ Admin Module APIs (9–12)

| API No | Method | Endpoint |
|-------|--------|----------|
| 9  | PUT | `/api/v1/admin/restaurants/1/approve` |
| 10 | PUT | `/api/v1/admin/restaurants/1/disable` |
| 11 | GET | `/api/v1/admin/feedback` |
| 12 | GET | `/api/v1/admin/orders` |

---

### ✅ User / Customer Module APIs (13–16)

| API No | Method | Endpoint |
|-------|--------|----------|
| 13 | POST | `/api/v1/users/register` |
| 14 | GET  | `/api/v1/restaurants/search?name=Food` |
| 15 | POST | `/api/v1/orders` |
| 16 | POST | `/api/v1/ratings` |

---

### ✅ Order Module APIs (17–18)

| API No | Method | Endpoint |
|-------|--------|----------|
| 17 | GET | `/api/v1/restaurants/1/orders` |
| 18 | GET | `/api/v1/users/1/orders` |

---

---

# 🧪 API Testing Documentation

This project includes complete testing of all 18 Foodie App REST APIs using:

- ✅ Postman (Manual Testing)
- ✅ Robot Framework (Automation Testing)
- ✅ Pytest (Automation Testing)

---

## ✅ 1. Postman Manual API Testing

All APIs were tested manually using **Postman** to verify:

- Request Body Validation  
- Correct Response Output  
- Proper Status Codes  
- Module Workflow Execution  

### 📌 Steps to Run Postman Testing

1. Open **Postman**
2. Click **Import**
3. Select the collection file:

postman/foodie.collection.json: 


4. Run APIs one by one in this order:

- Register Restaurant  
- Add Dish  
- Register User  
- Place Order  
- Give Rating  
- View Orders  

---

### ✅ Postman Tested APIs Include:

- Restaurant Module APIs (1–4)
- Dish Module APIs (5–8)
- Admin Module APIs (9–12)
- User Module APIs (13–16)
- Order Module APIs (17–18)

---

---

## 🤖 Robot Framework Automation Testing

Robot Framework was used to perform **keyword-driven automation testing** for all 18 Foodie App REST APIs.

This suite validates:

- API Status Codes  
- JSON Request/Response Handling  
- Complete Workflow Execution  

---

### 📌 Robot Framework Tools Used

- Robot Framework  
- RequestsLibrary  

---

### 🔧 Installation

Install Robot Framework and RequestsLibrary using:

```bash
pip install robotframework
pip install robotframework-requests

---
Robot Test File Location

All Robot automation scripts are available inside:

robot_tests/foodie.robot

---
Execute Robot Suite

robot foodie.robot

Expected Output
18 tests, 18 passed, 0 failed


---


---

---

# ✅ COPY-PASTE: PYTEST AUTOMATION TESTING SECTION

```md
---

## 🧪 Pytest Automation Testing

Pytest was used to perform **Python-based REST API automation testing** for all Foodie App endpoints.

Pytest validates:

- API Response Status Codes  
- JSON Response Data  
- End-to-End API Workflow  

---

### 📌 Pytest Tools Used

- Pytest Framework  
- Python Requests Module  

---

### 🔧 Installation

Install Pytest and Requests library:

```bash
pip install pytest requests

---
Pytest File Location

All Pytest automation scripts are available inside:

test_pytest/test_foodie.py

Run Pytest Automation

pytest -v

Expected Output
18 passed, 0 failed
