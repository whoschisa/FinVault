# 🏦 Fin-Vault – Personal Banking & Expense Manager (Python + MySQL)

Fin-Vault is a terminal-based banking and personal finance management system built using **Python, MySQL, and CSV files**.  
It simulates real-world banking operations like account creation, login, deposits, withdrawals, expense tracking, and admin control — all through a CLI.

---

# 🚀 FEATURES

## 👤 User Features
- Create a new account with username and password  
- Secure login system with limited password attempts  
- Deposit money into account (stored in MySQL)  
- Withdraw money with balance validation  
- Log personal expenses by category  
- View full bank statement (transaction history)  
- Track expenses using Matplotlib graphs  
- View account details (account number, balance, date of joining)  
- Help section for guidance  

## 🛠 Admin Features
- Admin login system  
- View all registered users  
- View total assets in the system  
- Delete users (MySQL + CSV + table cleanup)

---

# 🧠 TECH STACK
- Python 3  
- MySQL (mysql-connector-python)  
- CSV file handling  
- Matplotlib (data visualization)  
- PrettyTable (CLI tables)  
- PIL (image handling)  
- Built-in Python libraries (datetime, random, time, collections)

---

# 🗄 DATABASE STRUCTURE

## Users Table
- account (INT)  
- balance (DECIMAL)  
- doj (DATETIME)  
- username (VARCHAR)

## User Transaction Table (per user)
- id (AUTO_INCREMENT)  
- logs (VARCHAR)  
- balance (DECIMAL)  
- date (DATE)

---

# 📊 EXPENSE TRACKING
Expenses are visualized using **Matplotlib graphs**, helping users analyze spending patterns over time.

---

# 📁 PROJECT FILES
- finvault.py → Main application  
- data.csv → User credentials  
- admin.csv → Admin credentials  
- help_file.txt → Help documentation  
- fin-vault-img.png → UI/logo image  

---

# ⚙️ SETUP INSTRUCTIONS

## 1. Clone Repository
git clone https://github.com/yourusername/fin-vault.git  
cd fin-vault  

## 2. Install Dependencies
pip install mysql-connector-python matplotlib pillow prettytable  

## 3. Create Database
CREATE DATABASE finvault;

CREATE TABLE users (
account INT PRIMARY KEY,
balance DECIMAL(10,2),
doj DATETIME,
username VARCHAR(50)
);

## 4. Run Project
python finvault.py

---

# 🔐 SECURITY NOTES
- Passwords stored in CSV (NOT encrypted — for learning purposes)  
- Each user has a separate transaction table  
- Admin authentication handled separately  

---

# 🚀 FUTURE IMPROVEMENTS
- Password hashing (bcrypt)  
- Cloud database integration  
- GUI version (Tkinter / Web app)  
- PDF bank statements  
- Advanced analytics dashboard  

---

# 💡 PURPOSE
This project simulates a real banking system using Python + MySQL and demonstrates:
- Database handling  
- Authentication systems  
- File management  
- Data visualization  
- CLI system design  

---

# 👨‍💻 AUTHOR
Fin-Vault Developer  
Built as a Python + SQL learning project for understanding real-world system architecture.
