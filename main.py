import mysql.connector as mycon
import random
import csv
import time
from datetime import date, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
import os
day = date.today()


con = mycon.connect(
    host="localhost",
    user="root",
    passwd="0000",
    database="finvault"
)

if con.is_connected():
    print("[LOGS] : Database Connected")
    

cur = con.cursor()

def printbw(content):
    terminal_width = os.get_terminal_size().columns
    content_width = len(content)

    if content_width >= terminal_width:
        print(content)
    else:
        padding_width = (terminal_width - content_width) // 2
        padding = " " * padding_width
        print(padding + content + padding)


def signup():
    global username                                                     # This will be the global username
    global doj                                                          # This will be the join date
    while True:
        printbw(r"╔════════════════════════════════════════════════════════════╗")
        printbw(r"║                Enter your desired username:                ║")
        printbw(r"╚════════════════════════════════════════════════════════════╝")
        username = input("INPUT:")
        with open("data.csv", "r") as file:
            read = csv.reader(file)
            rows = list(read)
            items = [row[0] for row in rows]

        if username in items:
            time.sleep(0.18)
            printbw(r"╔════════════════════════════════════════════════════════════╗")
            printbw(r"║                    Username already exists.                ║")
            printbw(r"╚════════════════════════════════════════════════════════════╝")
            continue
        
        if len(username) > 20:
            time.sleep(0.18)
            printbw(r"╔════════════════════════════════════════════════════════════╗")
            printbw(r"║                Username should be of max                   ║")
            printbw(r"║                   20 characters                            ║")
            printbw(r"╚════════════════════════════════════════════════════════════╝")
            continue
        
        break


    while True:
        time.sleep(0.18)
        printbw(r"╔════════════════════════════════════════════════════════════╗")
        printbw(r"║                  Enter a valid password:                   ║")
        printbw(r"╚════════════════════════════════════════════════════════════╝")

        pwd = input(" ")

        time.sleep(0.18)
        printbw(r"╔══════════════════════════════════════════════════════════════╗")
        printbw(r"║                      Confirm Password                        ║")
        printbw(r"╚══════════════════════════════════════════════════════════════╝")

        confirm_pwd = input(" ")

        if pwd != confirm_pwd:
            time.sleep(0.18)
            printbw(r"╔══════════════════════════════════════════════════════════════╗")
            printbw(r"║                   Passwords do not match                     ║")
            printbw(r"╚══════════════════════════════════════════════════════════════╝")
            continue

        break

    while True:
        data = [username, pwd]
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            cur.execute(f"CREATE TABLE `{username}` (account INTEGER primary key, balanc DECIMAL(10,2) DEFAULT 0.00, doj DATE );")
            con.commit()
            menu()

            continue


            # Code in Progress

def welcome():
    while True:
        printbw(r"╔════════════════════════════════════════════════════════════╗")
        printbw(r"║  ______  _                __      __               _  _    ║")
        printbw(r"║ |  ____|(_)               \ \    / /              | || |   ║")
        printbw(r"║ | |__    _  _ __   ______  \ \  / /   __ _  _   _ | || |_  ║")
        printbw(r"║ |  __|  | || '_ \ |______|  \ \/ /   / _` || | | || || __| ║")
        printbw(r"║ | |     | || | | |           \  /   | (_| || |_| || || |_  ║")
        printbw(r"║ |_|     |_||_| |_|            \/     \__,_| \__,_||_| \__| ║")
        printbw(r"║                                                            ║")
        printbw(r"╚════════════════════════════════════════════════════════════╝")
        time.sleep(0.2)
        printbw(r"╔═════════════════════════════════════════════════════════════╗")
        printbw(r"║           Welcome! How can we assist you today?             ║")
        printbw(r"╚═════════════════════════════════════════════════════════════╝")
        time.sleep(0.2)
        printbw(r"╔════════════════════════════════════════════════════════════╗")
        printbw(r"║                 1. Open an Account                         ║")
        printbw(r"║                 2. Login to your Account                   ║")
        printbw(r"║                 3. Exit the App                            ║")
        printbw(r"╚════════════════════════════════════════════════════════════╝")


        choice = input("Enter Your Choice: ")
        if choice == "1":
            signup()
            return
        elif choice == "2":
            return
        elif choice == "3":
            printbw(r"╔════════════════════════════════════════════════════════════╗")
            printbw(r"║  ______  _                __      __               _  _    ║")
            printbw(r"║ |  ____|(_)               \ \    / /              | || |   ║")
            printbw(r"║ | |__    _  _ __   ______  \ \  / /   __ _  _   _ | || |_  ║")
            printbw(r"║ |  __|  | || '_ \ |______|  \ \/ /   / _` || | | || || __| ║")
            printbw(r"║ | |     | || | | |           \  /   | (_| || |_| || || |_  ║")
            printbw(r"║ |_|     |_||_| |_|            \/     \__,_| \__,_||_| \__| ║")
            printbw(r"║                                                            ║")
            printbw(r"╚════════════════════════════════════════════════════════════╝")
            time.sleep(0.2)
            print("╔═════════════════════════════════════════════╗")
            print("║        Thank You For Using PY - FIT         ║")
            print("╚═════════════════════════════════════════════╝")
            quit()
        else:
            print("╔═══════════════════════════════════════╗")
            print("║ Invalid input. Please choose a number ║")
            print("║             from 1 to 3.              ║")
            print("╚═══════════════════════════════════════╝")

def menu():
    while True:
        print("Hi")


welcome()