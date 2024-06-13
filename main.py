import mysql.connector as mycon
import random
from prettytable import PrettyTable
import csv
import time
from datetime import date, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
import os

con = mycon.connect(
    host="localhost",
    user="root",
    passwd="0000",
    database="finvault"
)

if con.is_connected():
    print("[LOGS] : Database Connected")

cur = con.cursor()

#Sign-up Function
def signup():
    global username                                                     # This will be the global username
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                Enter your desired username:                ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        username = input("INPUT:")
        with open("data.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)
            items = [row[0] for row in rows]

        if username in items:
            time.sleep(0.18)
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║                    Username already exists.                ║")
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

        pwd = input(" ")

        time.sleep(0.18)
        print(r"╔══════════════════════════════════════════════════════════════╗")
        print(r"║                      Confirm Password                        ║")
        print(r"╚══════════════════════════════════════════════════════════════╝")

        confirm_pwd = input(" ")

        if pwd != confirm_pwd:
            time.sleep(0.18)
            print(r"╔══════════════════════════════════════════════════════════════╗")
            print(r"║                   Passwords do not match                     ║")
            print(r"╚══════════════════════════════════════════════════════════════╝")
            continue

        break

    data = [username, pwd]
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    cur.execute(f"CREATE TABLE `{username}` (account INTEGER primary key, balanc DECIMAL(10,2) DEFAULT 0.00, doj DATE );")
    con.commit()

    menu()

#Login Function
def login():
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                   Enter your username:                     ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        input_username = input(" ")
        with open("data.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)
            items = [row[0] for row in rows]


def welcome():
    while True:
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║  ______  _                __      __               _  _    ║")
        print(r"║ |  ____|(_)               \ \    / /              | || |   ║")
        print(r"║ | |__    _  _ __   ______  \ \  / /   __ _  _   _ | || |_  ║")
        print(r"║ |  __|  | || '_ \ |______|  \ \/ /   / _` || | | || || __| ║")
        print(r"║ | |     | || | | |           \  /   | (_| || |_| || || |_  ║")
        print(r"║ |_|     |_||_| |_|            \/     \__,_| \__,_||_| \__| ║")
        print(r"║                                                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        time.sleep(0.2)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║           Welcome! How can we assist you today?            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")
        time.sleep(0.2)
        print(r"╔════════════════════════════════════════════════════════════╗")
        print(r"║                 1. Open an Account                         ║")
        print(r"║                 2. Login to your Account                   ║")
        print(r"║                 3. Exit the App                            ║")
        print(r"╚════════════════════════════════════════════════════════════╝")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            signup()
            return
        elif choice == "2":
            return
        elif choice == "3":
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║  ______  _                __      __               _  _    ║")
            print(r"║ |  ____|(_)               \ \    / /              | || |   ║")
            print(r"║ | |__    _  _ __   ______  \ \  / /   __ _  _   _ | || |_  ║")
            print(r"║ |  __|  | || '_ \ |______|  \ \/ /   / _` || | | || || __| ║")
            print(r"║ | |     | || | | |           \  /   | (_| || |_| || || |_  ║")
            print(r"║ |_|     |_||_| |_|            \/     \__,_| \__,_||_| \__| ║")
            print(r"║                                                            ║")
            print(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(0.2)
            print(r"╔═════════════════════════════════════════════════════════════╗")
            print(r"║             Thank You for using Fin - Vault                 ║")
            print(r"╚═════════════════════════════════════════════════════════════╝")
            quit()
        else:
            print(r"╔════════════════════════════════════════════════════════════╗")
            print(r"║               Invalid Input, Please choose                 ║")
            print(r"║                   options from 1 - 3                       ║")
            print(r"╚════════════════════════════════════════════════════════════╝")

def menu():
    print("Hi")

welcome()