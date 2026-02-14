# Expense Management System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Pytest](https://img.shields.io/badge/Testing-Pytest-brightgreen)
![Tests](https://img.shields.io/badge/Tests-Passing-success)

A full-stack Expense Management System built using Streamlit, FastAPI, and MySQL.


## 1. Project Description

The **Expense Management System** is a full-stack web application designed to help users record, manage, and analyze their daily expenses efficiently.

This system provides an interactive interface where users can:

- Add and update expenses
- Track spending patterns
- View category-wise and monthly analytics
- Explore an advanced dashboard with visual insights

The project is built using modern technologies including **Streamlit** for the frontend, **FastAPI** for the backend, and **MySQL** as the database.

---

## 2. Project Highlights

✅ Full-stack architecture (Frontend + Backend + Database)  
✅ Expense entry and update functionality  
✅ Category-based expense analytics  
✅ Monthly spending summaries  
✅ Advanced analytics dashboard with interactive charts  
✅ REST API integration using FastAPI  
✅ MySQL database connectivity  
✅ Modular and scalable project structure  
✅ Backend unit testing included  

---

## 3. Dataset Information & Credit

The dataset used in this project was provided as part of the course **Gen AI & Data Science Bootcamp**, conducted by **Codebasics**.

Full credit goes to the **Mr. Dhaval Patel** and the Codebasics team for providing the dataset and learning resources.

> **Note:** The dataset is not publicly available and is therefore not included in this GitHub repository due to sharing restrictions.

This project is created strictly for educational and portfolio demonstration purposes.


---

## 4. Tools & Technologies Used / Tech Stack

| Layer/Component | Technology |
|----------------|------------|
| Frontend UI     | Streamlit |
| Backend API     | FastAPI |
| Server Runner   | Uvicorn |
| Database        | MySQL |
| Data Analysis   | Pandas |
| Visualization   | Plotly |
| Testing         | Pytest |
| Logging         | Python Logging Module |

---

## 5. Project Structure & Workflow

### 5.1 Folder Structure

### Expense_Management_System/
- Backend/
  - db_helper.py # Database connection and queries
  - logging_setup.py # Logging configuration
  - server.py # FastAPI backend server
  - server.log # Generated log file (ignored in GitHub)
  - tests_backend/
    - test_db_helper.py # Backend unit tests
    
- Frontend/
  - app.py # Main Streamlit entry point
  - add_update.py # Add & update expenses module
  - analytics_by_category.py # Category-wise analytics module
  - analytics_by_months.py # Monthly-wise analytics module
  - analytics_dashboard.py # Advanced dashboard module
  - tests_frontend/
    - (Reserved for future frontend tests)

- Images/ # Project screenshots

- requirements.txt # Project dependencies

- README.md # Project documentation

### 5.2 Project Workflow

1. User enters expense details in the Streamlit frontend  
2. Streamlit sends requests to FastAPI backend  
3. Backend processes data and stores it in MySQL  
4. Analytics endpoints compute summaries  
5. Dashboard displays insights through interactive Plotly charts  

---

## 6. Core Features

### Expense Management
- Add new expenses by date, category, and amount  
- Update existing expense records  

### Analytics Modules

The frontend includes 4 main functional components:

1. **Add & Update Expenses**
2. **Analytics by Category**
3. **Analytics by Months**
4. **Advanced Analytics Dashboard**

### Dashboard Insights
- KPI summary cards  
- Monthly spending trend chart  
- Category distribution donut chart  
- Stacked monthly-category visualization  
- Top 10 largest expenses bar chart 

---

## 7. Project Screenshots

### Add & Update Expenses
![Add Update Page](Images/add_update_frontend.png)

### Category Analytics
![Category Analytics](Images/analytics_by_category.png)

### Monthly Expense Trends
![Monthly Summary](Images/analytics_by_months.png)

### Analytics Dashboard
![Dashboard Preview](Images/analytics_dashboard.png)

---

## 8. Installation & Setup Instructions

Follow these steps to run the project locally.

---

### Step 1: Clone the Repository
In terminal:

    git clone https://github.com/yourusername/expense-management-system.git
    cd expense-management-system

### Step 2: Install Required Dependencies
In terminal:

    pip install -r requirements.txt

### Step 3: Configure MySQL Database
This project uses **MySQL** as the backend database to store expense records.

#### 3.1 Create a Database

Log in to MySQL and create a new database:

    CREATE DATABASE your_database;

You must create the required **expenses** table before running the project.

#### 3.2 Update Database Credentials
Open the following file:
    
    Backend/db_helper.py

Update your MySQL connection details:
    
    connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
    )

**Note:** Replace **your_password** with your local MySQL password before running the application.

#### 3.3 Start MySQL Service
Ensure that your MySQL server is running locally, otherwise the backend API will not be able to connect to the database.

### Step 4: Start the Backend Server
In terminal:

    cd Backend
    uvicorn server:app --reload

### Step 5: Start the Frontend Server
Open a new terminal:

    cd Frontend
    streamlit run app.py

---

## 9. Testing

Backend unit tests are included to validate database helper functions.

### Run Backend Tests

From the project root directory, execute:

In terminal:

    python -m pytest Backend/tests_backend

Expected output:

    3 passed in 0.23s

---

## 10. Conclusion

The **Expense Management System** is a complete full-stack application that demonstrates:

- Expense tracking and management
- REST API development using FastAPI
- Database integration with MySQL
- Interactive analytics dashboards with Streamlit and Plotly

This project showcases strong skills in full-stack development, backend engineering, and data-driven visualization.

---









