import mysql.connector as mycon
import random
import csv
import time
from datetime import date, timedelta
from tabulate import tabulate
import matplotlib.pyplot as plt
import os

con = mycon.connect(
    host="localhost",
    user="root",
    passwd="0000"
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
        printbw("╔═════════════════════════════════════════════╗")
        printbw("║         Enter your desired username:        ║")
        printbw("╚═════════════════════════════════════════════╝")
        username = input("INPUT:")
        with open("data.csv", "r") as file:
            read = csv.reader(file)
            user_row = list(read)
            items = [row[0] for row in user_row]

        if username in items:
            time.sleep(0.18)
            print("╔═════════════════════════════════════════════╗")
            print("║           Username already exists.          ║")
            print("╚═════════════════════════════════════════════╝")
            continue
        
        if len(username) > 20:
            time.sleep(0.18)
            print("╔═════════════════════════════════════════════╗")
            print("║         Username should be of max.          ║")
            print("║               20 characters                 ║")
            print("╚═════════════════════════════════════════════╝")
            continue
        
        break
    

    while True:
        time.sleep(0.18)
        print("╔═══════════════════════════════════════╗")
        print("║        Enter a valid password:        ║")
        print("╚═══════════════════════════════════════╝")

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


welcome()