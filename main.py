import mysql.connector as mycon
import random
import csv
from datetime import datetime, date
from tabulate import tabulate
from PIL import Image
import matplotlib.pyplot as plt
import time
from prettytable import PrettyTable
from collections import defaultdict

# Database connection
con = mycon.connect(
    host="localhost",
    user="root",
    passwd="0000",
    database="finvault"
)

if con.is_connected():
    print("[LOGS] : Database Connected")

cur = con.cursor()

def display_image(image_path):
    image = Image.open(image_path)
    image.show()

image_path = r"C:\Users\dell\Desktop\fin-vault\fin-vault-img.png"
display_image(image_path)

def generate_account(cursor):
    while True:
        account_number = random.randint(1000, 9999)
        
        cursor.execute(f"SELECT * FROM users WHERE account = {account_number}")
        if cursor.fetchone() is None:
            return account_number
        
def fin_vault():
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║  ______  _                __      __               _  _    ║")
        print(r"║ |  ____|(_)               \ \    / /              | || |   ║")
        print(r"║ | |__    _  _ __   ______  \ \  / /   __ _  _   _ | || |_  ║")
        print(r"║ |  __|  | || '_ \ |______|  \ \/ /   / _` || | | || || __| ║")
        print(r"║ | |     | || | | |           \  /   | (_| || |_| || || |_  ║")
        print(r"║ |_|     |_||_| |_|            \/     \__,_| \__,_||_| \__| ║")
        print(r"║                                                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")

        
def welcome():
    while True:
        fin_vault()
        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║           Welcome! How can we assist you today?            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                 1. Open an Account                         ║")
        print(r"║                 2. Login to your Account                   ║")
        print(r"║                 3. Admin Login                             ║")
        print(r"║                 4. Exit the App                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            signup()
            return
        elif choice == "2":
            login()
            return
        elif choice == "3":
            admin()
            return
        elif choice == "4":
            fin_vault()
            time.sleep(0.2)
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(r"║             Thank You for using Fin - Vault                 ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            quit()
        else:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║               Invalid Input, Please choose                 ║")
            print(r"║                   options from 1 - 4                       ║")
            print(r"╚════════════════════════════════════════════════════════════╝")


def signup():
    global username
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                Enter your desired username:                ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        username = input("INPUT:")
        
        with open(r"C:\Users\dell\Desktop\fin-vault\data.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)
            items = [row[0] for row in rows]

        if username in items:
            time.sleep(0.18)
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                   Username already exists.                 ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            continue

        if len(username) > 20:
            time.sleep(0.18)
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                Username should be of max                   ║")
            print(r"║                   20 characters                            ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            continue

        break

    while True:
        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                  Enter a valid password:                   ║")
        print(r"╚════════════════════════════════════════════════════════════╝")


        pwd = input("INPUT:")

        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                     Confirm Password                       ║")
        print(r"╚════════════════════════════════════════════════════════════╝")

        confirm_pwd = input("INPUT:")

        if pwd != confirm_pwd:
            time.sleep(0.18)
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                  Passwords do not match                    ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            continue

        break

    data = [username, pwd]
    with open(r'C:\Users\dell\Desktop\fin-vault\data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    
    unique_account = generate_account(cur)
    doj = datetime.now()
    cur.execute("INSERT INTO users (account, balance, doj, username) VALUES (%s, %s, %s, %s)",
                (unique_account, 0.00, doj, username))
    cur.execute(f"CREATE TABLE `{username}` (id INT AUTO_INCREMENT PRIMARY KEY,"
    "logs VARCHAR(20), balance DECIMAL(10, 2) DEFAULT 0.00, date DATE);")

    con.commit()
    print(r"╔════════════════════════════════════════════════════════════╗")
    print(r"║                Account Created successfully!               ║")
    print(r"╚════════════════════════════════════════════════════════════╝")
    time.sleep(1.0)
    menu()

def login():
    global username 
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                   Enter your username:                     ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        input_username = input("INPUT: ")
        
        with open(r"C:\Users\dell\Desktop\fin-vault\data.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)

        user_exists = False
        for row in rows:
            if input_username == row[0]:
                user_exists = True
                attempt_count = 0
                while attempt_count < 3:
                    time.sleep(0.18)
                    print(r"╔════════════════════════════════════════════════════════════╗")
                    print(r"║                   Enter your password:                     ║")
                    print(r"╚════════════════════════════════════════════════════════════╝")
                    password = input("INPUT: ")
                    if password == row[1]:
                        time.sleep(0.18)
                        print(r"╔════════════════════════════════════════════════════════════╗")
                        print(r"║                     Login Successful                       ║")
                        print(r"╚════════════════════════════════════════════════════════════╝")
                        username = input_username
                        time.sleep(1.0)
                        menu()  
                        return
                    else:
                        attempt_count += 1
                        print(r"╔════════════════════════════════════════════════════════════╗")
                        print(f"║      Invalid Password. {3 - attempt_count} attempts left.  ║")
                        print(r"╚════════════════════════════════════════════════════════════╝")
                        if attempt_count >= 3:
                            print(r"╔════════════════════════════════════════════════════════════╗")
                            print(r"║          Too many failed attempts. Please try again later. ║")
                            print(r"╚════════════════════════════════════════════════════════════╝")
                            time.sleep(1)
                            return
                        
                        print(r"Invalid Password. {3 - attempt_count} attempts left.")
                        print(r"Too many failed attempts. Please try again later.")
                        
                        time.sleep(1)
                        return
                    else:
                        

                break  

        if not user_exists:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                   Username not found!                      ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(0.18)
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║            Do you want to create a new account             ║")
            print(r"║                   (y) - yes . (n) - no                     ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            choice = input("INPUT: ").lower()
            if choice == "y":
                signup()
                return
            else:
                fin_vault()
                time.sleep(0.2)
                print(r"╔═════════════════════════════════════════════════════════════╗")
                print(r"║             Thank You for using Fin - Vault                 ║")
                print(r"╚═════════════════════════════════════════════════════════════╝")
                quit()
                

def admin():
    global adminusername 
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                   Enter your username:                     ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        input_username = input("INPUT: ")
        
        with open(r"C:\Users\dell\Desktop\fin-vault\admin.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)

        user_exists = False
        for row in rows:
            if input_username == row[0]:
                user_exists = True
                attempt_count = 0
                while attempt_count < 3:
                    time.sleep(0.18)
                    print(r"╔════════════════════════════════════════════════════════════╗")
                    print(r"║                   Enter your password:                     ║")
                    print(r"╚════════════════════════════════════════════════════════════╝")
                    password = input("INPUT: ")
                    if password == row[1]:
                        time.sleep(0.18)
                        print(r"╔════════════════════════════════════════════════════════════╗")
                        print(r"║                     Login Successful                       ║")
                        print(r"╚════════════════════════════════════════════════════════════╝")
                        username = input_username
                        time.sleep(1.0)
                        admin_menu() 
                        return
                    else:
                        attempt_count += 1
                        print(r"╔════════════════════════════════════════════════════════════╗")
                        print(f"║      Invalid Password. {3 - attempt_count} attempts left.  ║")
                        print(r"╚════════════════════════════════════════════════════════════╝")
                        if attempt_count >= 3:
                            print(r"╔════════════════════════════════════════════════════════════╗")
                            print(r"║          Too many failed attempts. Please try again later. ║")
                            print(r"╚════════════════════════════════════════════════════════════╝")
                            time.sleep(1)
                            return
                    break      
            
            
def admin_menu():
    while True:
        fin_vault()
        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                                                            ║")
        print(r"║                    1. Show Users                           ║")
        print(r"║                                                            ║")
        print(r"║                    2. Show Total Assets                    ║")
        print(r"║                                                            ║")
        print(r"║                    3. Delete Users                         ║")
        print(r"║                                                            ║")
        print(r"║                    4. Quit                                 ║")
        print(r"║                                                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        print("INPUT : ", end="")
        try:
            choice = int(input())
            if choice == 1:
                show_users()
            elif choice == 2:
                total_assets()
            elif choice == 3:
                delete_users()
                time.sleep(0.2)
                print(r"╔═════════════════════════════════════════════════════════════╗")
                print(r"║             Thank You for using Fin - Vault                 ║")
                print(r"╚═════════════════════════════════════════════════════════════╝")
                quit()
            else:
                print(r"╔════════════════════════════════════════════════════════════╗")
                print(r"║                   Invalid choice. Try again!               ║")
                print(r"╚════════════════════════════════════════════════════════════╝")
        except ValueError:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                  Please enter a valid number!              ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
        

def show_users():
    try:
        cur.execute(f"SELECT account,username,doj FROM users;")
        results = cur.fetchall()  

        if len(results) == 0:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║           [INFO] No Users found in your database.          ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            return

        table = PrettyTable()
        table.field_names = ["Account Number", "Username", "Date of Joining"]

        for row in results:
            account, username, doj = row
            table.add_row([account, username, doj])

        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                Current User Date is below:                 ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        print(table)
        time.sleep(5.0)
        
    except Exception as e:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(f"    [ERROR] An error occurred: {str(e)}.   ")
        print(r"╚════════════════════════════════════════════════════════════╝")


def total_assets():
    try:
        cur.execute("SELECT SUM(balance) FROM users;")
        result = cur.fetchone()[0]  

        table = PrettyTable()
        table.field_names = ["Total Assets Under the Bank"]

        if result is None:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║           [INFO] No Assets found in your database.         ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            return

        table.add_row([result]) 

        print(table)
        time.sleep(5.0)
        
    except Exception as e:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(f"    [ERROR] An error occurred: {str(e)}.   ")
        print(r"╚════════════════════════════════════════════════════════════╝")


def menu():
    current_date = date.today() 
    
    while True:
        fin_vault()
        time.sleep(0.18)
        print(f"╔════════════════════════════════════════════════════════════╗")
        print(f"                      Welcome {username}                       ")
        print(f"╚════════════════════════════════════════════════════════════╝")
        time.sleep(0.18)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                                                            ║")
        print(r"║                    1. Deposit Balance                      ║")
        print(r"║                                                            ║")
        print(r"║                    2. Withdraw Balance                     ║")
        print(r"║                                                            ║")
        print(r"║                    3. Log Expenses                         ║")
        print(r"║                                                            ║")
        print(r"║                    4. Bank Statement                       ║")
        print(r"║                                                            ║")
        print(r"║                    5. Account Details                      ║")
        print(r"║                                                            ║")
        print(r"║                    6. About the App                        ║")
        print(r"║                                                            ║")
        print(r"║                    7. Track Expenses                       ║")
        print(r"║                                                            ║")
        print(r"║                    8. Quit                                 ║")
        print(r"║                                                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        print("INPUT : ", end="")
        user = username
        
        try:
            choice = int(input())
            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                log_expenses()
            elif choice == 4:
                bank_statement()
            elif choice == 5:
                account_details()
            elif choice == 6:
                help()
            elif choice == 7:
                track_expenses()
            elif choice == 8:
                fin_vault()
                time.sleep(0.2)
                print(r"╔═════════════════════════════════════════════════════════════╗")
                print(r"║             Thank You for using Fin - Vault                 ║")
                print(r"╚═════════════════════════════════════════════════════════════╝")
                welcome()
            else:
                print(r"╔════════════════════════════════════════════════════════════╗")
                print(r"║                   Invalid choice. Try again!               ║")
                print(r"╚════════════════════════════════════════════════════════════╝")
        except ValueError:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                  Please enter a valid number!              ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            

def deposit():
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║   Enter the amount you want to deposit: [exit to Exit]     ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        amount = input("INPUT: AED ")

        if amount.lower() == 'exit':
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(f"║              [EXIT] Cancelling Deposit.                    ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(1.0)
            break

        try:
            amount_float = int(amount)
            
            # Updating users table with new balance
            cur.execute("UPDATE users SET balance = balance + %s WHERE username = %s;", (amount_float, username))
            # Adding it into logs for that specifc user (will be accessible later)
            cur.execute(f"INSERT INTO {username} (logs, balance, date) VALUES (%s, %s, NOW());", (f"Deposited", amount))
            con.commit()

            print(r"╔════════════════════════════════════════════════════════════╗")
            print(f"                   Deposit of AED {amount_float} successful.         ")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(1.0)
            break

        except ValueError:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║    [ERROR] Invalid input. Please enter a valid amount.     ║")
            print(r"╚════════════════════════════════════════════════════════════╝")

        except Exception as e:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(f"    [ERROR] An error occurred: {str(e)}.   ")
            print(r"╚════════════════════════════════════════════════════════════╝")

def withdraw():
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║   Enter the amount you want to withdraw: [exit to Exit]    ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        amount = input("INPUT: AED ")

        if amount.lower() == 'exit':
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(f"║              [EXIT] Cancelling Withdrawal.                 ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(1.0)
            break

        try:
            amount_float = int(amount)
            
            # Updating users table with new balance
            cur.execute("""UPDATE users SET balance = balance - %s WHERE username = %s AND balance >= %s;""",
                        (amount_float, username, amount_float))

            if cur.rowcount == 0:  
                print(r"╔════════════════════════════════════════════════════════════╗")
                print(f"║               [ERROR] Insufficient balance.                ║")
                print(r"╚════════════════════════════════════════════════════════════╝")
                continue

            # Adding it into logs with the name WITHDRAWN which can be viewed later.
            cur.execute(f"INSERT INTO {username} (logs, balance, date) VALUES (%s, %s, NOW());",
                        (f"Withdrawn", amount))
            con.commit()

            print(r"╔════════════════════════════════════════════════════════════╗")
            print(f"        Withdrawal of AED {amount_float} successful.          ")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(1.0)
            break

        except ValueError:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║    [ERROR] Invalid input. Please enter a valid amount.     ║")
            print(r"╚════════════════════════════════════════════════════════════╝")

def log_expenses():
    while True:
        fin_vault()
        time.sleep(0.2)
        print(r"╔═════════════════════════════════════════════════════════════╗")
        print(r"║                      Log Your Expenses                      ║")
        print(r"╚═════════════════════════════════════════════════════════════╝")
        time.sleep(0.2)
        
        # Get category input
        print(r"╔═════════════════════════════════════════════════════════════╗")
        print(r"║  Enter your expenditure category (ex: food, drinks, etc.)   ║")
        print(r"║                   Type 'exit' to Exit                       ║")
        print(r"╚═════════════════════════════════════════════════════════════╝")
        category = input("INPUT: ")
        
        if len(category) > 20:
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(r"║       Category can be a maximum of 20 characters only       ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            continue
        
        # Get amount input
        print(r"╔═════════════════════════════════════════════════════════════╗")
        print(r"║                Enter your expenditure amount:               ║")
        print(r"╚═════════════════════════════════════════════════════════════╝")
        try:
            amount = float(input("INPUT: AED "))
            if amount <= 0:
                print(r"╔═════════════════════════════════════════════════════════════╗")
                print(r"║         [ERROR] Amount must be greater than zero.           ║")
                print(r"╚═════════════════════════════════════════════════════════════╝")
                continue

        except ValueError:
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(r"║        [ERROR] Invalid input. Please enter a valid amount.  ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            continue

        try:
            cur.execute(f"INSERT INTO {username} (logs, balance, date) VALUES (%s, %s, NOW());",
                        (f"Spent On {category}", amount))
            con.commit()  # Save the changes
            
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(f"║    Expense of AED {amount:.2f} for {category} logged successfully.    ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            time.sleep(2.0)
            break

        except Exception as e:
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(f"║        [ERROR] Failed to log the expense: {str(e)}           ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            

def bank_statement():
    try:
        cur.execute(f"SELECT date, logs, balance FROM {username};")
        results = cur.fetchall()  # Fetch all results

        if len(results) == 0:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║           [INFO] No transactions found in your account.    ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            return

        # Create a PrettyTable to display the statement
        table = PrettyTable()
        table.field_names = ["Date of Transaction", "Transaction Details", "Amount Spent (AED)"]

        # Iterate through the results and add them to the table
        for row in results:
            date, logs, amount = row
            table.add_row([date, logs, f"{amount:.2f}"])

        # Print the statement in a neat format
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                Your Bank Statement is Below:               ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        print(table)
        time.sleep(5.0)

    except Exception as e:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(f"║        [ERROR] Failed to retrieve bank statement: {str(e)}  ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        

def account_details():
    global username
    cur.execute(f"SELECT account, balance, doj, username FROM users WHERE username = '{username}';")
    results = cur.fetchall()  
    
    table = PrettyTable()
    table.field_names = ["Account Number", "Username", "Amount (AED)", "Date of Joining"]
    
    for row in results:
        account, balance, doj, username = row
        table.add_row([account, username, balance, doj])
        
    print(r"╔════════════════════════════════════════════════════════════╗")
    print(r"║              Your Account Details Are Below:               ║")
    print(r"╚════════════════════════════════════════════════════════════╝")
    print(table)
    time.sleep(5.0)
        
def help():
    try:
        with open('help_file.txt', 'r') as file:
            contents = file.read() 

        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                    Help Information                        ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        print(contents) 
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                 End of Help Information                    ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        time.sleep(10.0)
        
    except FileNotFoundError:
        print("Error: Help file not found.")
        
        
def delete_users():
    try:
        cur.execute("SELECT account, username FROM users;")
        users = cur.fetchall()

        if not users:
            print("No users found in the database.")
            return

        table = PrettyTable()
        table.field_names = ["Account Number", "Username"]
        for user in users:
            table.add_row(user)

        print("Current Users:")
        print(table)

        account_to_delete = input("Enter the account number of the user to delete: ")

        cur.execute("SELECT username FROM users WHERE account = %s;", (account_to_delete,))
        user = cur.fetchone()

        if not user:
            print("Account not found. Please enter a valid account number.")
            return

        username = user[0] 

        cur.execute(f"DROP TABLE IF EXISTS {username};")
        print(f"Table '{username}' has been deleted.")

        cur.execute("DELETE FROM users WHERE account = %s;", (account_to_delete,))
        con.commit()
        print(f"User '{username}' has been deleted from the 'users' table.")

        csv_file = r'C:\Users\dell\Desktop\fin-vault\data.csv'
        rows = []

        with open(csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != username:  
                    rows.append(row)

        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"User '{username}' has been removed from the CSV file.")
        print("\nUser deletion process completed successfully.")

    except Exception as e:
        print(f"[ERROR] An error occurred: {str(e)}")

        
def track_expenses():
    try:
        cur.execute(f"SELECT date, logs, balance FROM {username} WHERE logs LIKE '%spent%';")
        results = cur.fetchall()

        if len(results) == 0:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║           [INFO] No expense transactions found.            ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            return

        dates = []
        amounts = []

        for row in results:
            date_obj, logs, amount = row  
            dates.append(f"{logs}")  
            amounts.append(amount)
            
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║            Expense Tracking Graph Generated Below.         ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        
        plt.figure(figsize=(12, 6))
        plt.bar(dates, amounts, color='lightcoral', label='Amount Spent (AED)')
        plt.xticks(rotation=90, ha='center', fontsize=8)  
        plt.xlabel('Transaction (Date & Details)')
        plt.ylabel('Amount Spent (AED)')
        plt.title('Expenses for Each Transaction Over Time')
        plt.grid(True, axis='y')  
        plt.tight_layout()
        plt.legend()
        plt.show()
        
        time.sleep(5.0)
        menu()

        
        
    except Exception as e:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(f"║        [ERROR] Failed to retrieve expenses: {str(e)}       ║")
        print(r"╚════════════════════════════════════════════════════════════╝")

# Start the application
welcome()
