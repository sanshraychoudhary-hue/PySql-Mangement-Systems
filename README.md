# 🏫 Canteen Management System (CMS)

The **Canteen Management System (CMS)** is a Python–MySQL based console application developed to automate billing, inventory management, and sales tracking for school and college canteens.

This system was **practically implemented to assist canteen workers in my school**, reducing manual effort, minimizing billing errors, and enabling efficient inventory control.

> ⚠️ Note: This project is intentionally implemented as a **single Python file** to keep the system simple, lightweight, and easy to deploy in real environments.

---

## 🚀 Features

- Automated billing system  
- Real-time inventory management  
- Unique Bill ID generation (date-based)  
- Stock update after each transaction  
- Bill re-print using Bill ID  
- Trending items analysis (day-wise sales)  
- Product sales tracking using SQL aggregation  
- Automatic database & table creation  
- Menu-driven console interface  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Database:** MySQL  
- **Connector:** PyMySQL  
- **Interface:** Console-based (CLI)  

---

## ⚙️ System Workflow

```text
User Input (Menu)
        ↓
Billing / Inventory Logic
        ↓
MySQL Database Operations
        ↓
Stock Update & Bill Storage
        ↓
Sales Analytics (Trending Items)
