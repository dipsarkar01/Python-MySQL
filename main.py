import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)
mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        userid INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(200) NOT NULL,
        address VARCHAR(600) NOT NULL,
        phone VARCHAR(12) NOT NULL,
        account_number VARCHAR(10) NOT NULL,
        balance VARCHAR(20) NOT NULL
    )
""")

print("=============================================================")
print("                    Welcome to XYZ Bank")
print("=============================================================")

print("1. To create new account")
print("2. To deposit cash")
print("3. To withdraw cash")
print("2. Exit")

inp = int(input("Enter your choice:- "))
if inp == 1:
    yes = "c"
    while yes.lower() == "c":
        a = input("Enter your name:- ")
        b = input("Enter your address:- ")
        c = input("Enter your phone number:- ")
        d = str(random.randint(1000000000, 9999999999))
        print(f"Congratulations {a}, your account is successfully created.")
        print(f"Your account number is {d}")

        sql = "INSERT INTO users (name, address, phone, account_number, balance) VALUES (%s, %s, %s, %s, '0')"
        val = (a, b, c, d)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        break
        # yes = input("Press 'c' to create another account or any other key to exit: ")