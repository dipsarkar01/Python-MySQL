from tkinter import *
from tkinter.messagebox import *
import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)
mycursor = mydb.cursor()

class App(Tk):
    def __init__(self):
        super().__init__()

        # Window configuration
        width, height = 1000, 800
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        self.geometry(f"{width}x{height}+{c_x}+{c_y}")
        self.resizable(False, False)
        self.title("Dip's Notepad")

        try:
            self.iconbitmap("clipboard.ico")
        except Exception:
            pass  # Ignore missing icon file

        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        # Account Menu
        acc_menu = Menu(menu_bar, tearoff=0)
        acc_menu.add_command(label= "Create New Account", command=self.create_new_acc)
        acc_menu.add_separator()
        acc_menu.add_command(label= "Check Balance", command=self.check_bal)
        acc_menu.add_command(label= "Deposit Cash", command=self.depo_cash)
        acc_menu.add_command(label= "Withdraw Cash", command=self.with_cash)
        acc_menu.add_separator()
        acc_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Account", menu=acc_menu)

        # KYC Menu
        kyc_menu = Menu(menu_bar, tearoff=0)
        kyc_menu.add_command(label="Update Address", command=self.update_add)
        kyc_menu.add_command(label="Update Phone Number", command=self.update_ph_no)
        kyc_menu.add_separator()
        kyc_menu.add_command(label="Update All", command=self.update_all)
        menu_bar.add_cascade(label="KYC", menu=kyc_menu)

        # Help Menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def about(self):
        showinfo(title="About", message="XYZ Bank\nVersion 1.0")

    def create_new_acc(self):
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

    def check_bal(self):
        acc_num = input("Enter your account number: ")
        mycursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_num,))
        result = mycursor.fetchone()
        if result:
            print(f"Your current balance is: {result[0]}")
        else:
            print("Account not found.")

    def depo_cash(self):
        acc_num = input("Enter your account number: ")
        bal = int(input("Enter your amount: "))
        sql = "UPDATE users SET balance = balance+%s WHERE account_number = %s"
        val = (bal,acc_num)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Successfully deposited")

    def with_cash(self):
        acc_num = input("Enter your account number: ")
        bal = int(input("Enter your amount: "))
        mycursor.execute("SELECT balance from users WHERE account_number = %s", (acc_num,))
        current_bal = mycursor.fetchone()
        if current_bal and current_bal[0]>= bal:
            sql = "UPDATE users set balance=balance-%s WHERE account_number = %s"
            mycursor.execute(sql, (bal,acc_num))
            mydb.commit()
            print("Successfully withdraw.")
        else:
            print("Insufficient balance! or Invalid account.")

    def update_add(self):
        acc_num = input("Enter your account number: ")
        f = input("Enter your new address: ")
        sql = "UPDATE users SET address = %s WHERE account_number = %s"
        val = (f, acc_num)
        mycursor.execute(sql, val)
        mydb.commit()
    
    def update_ph_no(self):
        acc_num = input("Enter your account number: ")
        g = input("Enter your new phone number: ")
        sql = "UPDATE users SET phone = %s WHERE account_number = %s"
        val = (g, acc_num)
        mycursor.execute(sql, val)
        mydb.commit()

    def update_all(self):
        acc_num = input("Enter your account number: ")
        f = input("Enter your new address: ")
        g = input("Enter your new phone number: ")
        sql = "UPDATE users SET address = %s, phone = %s WHERE account_number = %s"
        val = (f, g, acc_num)
        mycursor.execute(sql, val)
        mydb.commit()

if __name__ == "__main__":
    app = App()
    app.mainloop()