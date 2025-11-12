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

while True:
    print("\nOptions:")
    print("1. To create new account")
    print("2. Check balance")
    print("3. To deposit cash")
    print("4. To withdraw cash")
    print("5. Update account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = input("Enter your name: ")
        b = input("Enter your address: ")
        c = input("Enter your phone number: ")
        d = str(random.randint(1000000000, 9999999999))
        e = 0
        print(f"Congratulations {a}, your account is successfully created.")
        print(f"Your account number is {d}")
        sql = "INSERT INTO users (name, address, phone, account_number, balance)VALUES (%s, %s, %s, %s, %s)"
        val = (a, b, c, d, e)
        mycursor.execute(sql, val)
        mydb.commit()
        print("record inserted.")

    elif choice == 2:
        acc_num = input("Enter your account number: ")
        mycursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_num,))
        result = mycursor.fetchone()
        if result:
            print(f"Your current balance is: {result[0]}")
        else:
            print("Account not found.")

    elif choice == 3:
        acc_num = input("Enter your account number: ")
        bal = int(input("Enter your amount: "))
        sql = "UPDATE users SET balance = balance+%s WHERE account_number = %s"
        val = (bal,acc_num)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully deposited")

    elif choice == 4:
        acc_num = input("Enter your account number: ")
        bal = input("Enter your amount: ")
        mycursor.execute("SELECT balance from users WHERE account_number = %s", (acc_num,))
        current_bal = mycursor.fetchone()
        if current_bal and current_bal[0]>= bal:
        # if current_bal[0]>= bal:
            sql = "UPDATE users set balance=balance-%s WHERE account_number = %s"
            mycursor.execute(sql, (bal,acc_num))
            mydb.commit()
            print("Successfully withdraw.")
        else:
            print("Insufficient balance! or Invalid account.")
    
    elif choice == 5:
        acc_num = input("Enter your account number: ")
        mycursor.execute("SELECT * from users WHERE account_number = %s", (acc_num,))
        result = mycursor.fetchone()
        print("=============================================================")
        print("            --:Your current account details:--")
        print("=============================================================")
        print(f"Name: {result[1]}")
        print(f"Address: {result[2]}")
        print(f"Phone number: {result[3]}")
        print(f"Account no.: {result[4]}")
        print(f"Balance: {result[5]}")
        print("\nSelect an option to update") 
        print("1. Update address")
        print("2. Update phone number")
        print("3. Update all")

        sub_choice = int(input("Enter your choice: "))
        if sub_choice == 1:
            f = input("Enter your new address: ")
            sql = "UPDATE users SET %s WHERE account_number = %s"
            val = (f, acc_num)
            mycursor.execute(sql, val)
            mydb.commit()

    elif choice == 6:
        print("Exiting... Have a great day!")
        break
    
    else:
            print("Invalid option. Please try again.")