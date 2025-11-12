from tkinter import *
from tkinter.messagebox import showinfo, showerror
import mysql.connector
import random

# Database connection
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
        width, height = 800, 600
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        self.geometry(f"{width}x{height}+{c_x}+{c_y}")
        self.resizable(False, False)
        self.title("XYZ Bank")

        # Menu bar setup
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        acc_menu = Menu(menu_bar, tearoff=0)
        acc_menu.add_command(label="Create New Account", command=self.create_new_acc)
        acc_menu.add_command(label="Account Details", command=self.acc_det)
        acc_menu.add_separator()
        acc_menu.add_command(label="Check Balance", command=self.check_bal)
        acc_menu.add_command(label="Deposit Cash", command=self.depo_cash)
        acc_menu.add_command(label="Withdraw Cash", command=self.with_cash)
        acc_menu.add_separator()
        acc_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Account", menu=acc_menu)

        kyc_menu = Menu(menu_bar, tearoff=0)
        kyc_menu.add_command(label="Update Address", command=self.update_add)
        kyc_menu.add_command(label="Update Phone Number", command=self.update_ph_no)
        kyc_menu.add_command(label="Update All", command=self.update_all)
        menu_bar.add_cascade(label="KYC", menu=kyc_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: showinfo("About", "XYZ Bank\nVersion 1.0"))
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Main Frame
        self.main_frame = Frame(self)
        self.main_frame.pack(expand=True)

        Label(self.main_frame, text="Welcome to XYZ Bank", font=("Arial", 24, "bold")).pack(pady=40)
        Label(self.main_frame, text="Choose an option from the menu above.", font=("Arial", 14)).pack()

    # Utility: clear previous widgets
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_new_acc(self):
        self.clear_frame()

        Label(self.main_frame, text="Create New Account", font=("Arial", 20, "bold")).pack(pady=20)
        name_label = Label(self.main_frame, text="Name:")
        name_label.pack()
        name_entry = Entry(self.main_frame, width=40)
        name_entry.pack()

        addr_label = Label(self.main_frame, text="Address:")
        addr_label.pack()
        addr_entry = Entry(self.main_frame, width=40)
        addr_entry.pack()

        phone_label = Label(self.main_frame, text="Phone Number:")
        phone_label.pack()
        phone_entry = Entry(self.main_frame, width=40)
        phone_entry.pack()

        def save_account():
            name = name_entry.get()
            address = addr_entry.get()
            phone = phone_entry.get()
            acc_num = str(random.randint(1000000000, 9999999999))
            sql = "INSERT INTO users (name, address, phone, account_number, balance) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, (name, address, phone, acc_num, 0))
            mydb.commit()
            showinfo("Success", f"Account created successfully!\nAccount Number: {acc_num}")

        Button(self.main_frame, text="Create Account", command=save_account).pack(pady=20)

    def acc_det(self):
        self.clear_frame()
        Label(self.main_frame, text="Account Details", font=("Arial", 20, "bold")).pack(pady=20)
        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        def fetch_acc():
            acc_num = acc_entry.get()
            mycursor.execute("SELECT * FROM users WHERE account_number = %s", (acc_num,))
            result = mycursor.fetchone()
            if result:
                root = Tk()
                root.title("Account Details")
                # width, height = 800, 620
                width, height = 400, 200
                sys_width = self.winfo_screenwidth()
                sys_height = self.winfo_screenheight()
                c_x = int(sys_width / 2 - width / 2)
                c_y = int(sys_height / 2 - height / 2)
                root.geometry(f"{width}x{height}+{c_x}+{c_y}")
                root.resizable(False, False)
                Label(root, text="Account Details", font=("Arial", 20, "bold")).pack(pady=20)
                Label(root, text=f"Name: {result[1]}", font=("Arial", 10, "bold")).pack()
                Label(root, text=f"Address: {result[2]}", font=("Arial", 10, "bold")).pack()
                Label(root, text=f"Phone Number: {result[3]}", font=("Arial", 10, "bold")).pack()
                Label(root, text=f"Account Number: {result[4]}", font=("Arial", 10, "bold")).pack()

            else:
                showerror("Error", "Account not found!")

        Button(self.main_frame, text="Check Balance", command=fetch_acc).pack(pady=20)

    def check_bal(self):
        self.clear_frame()
        Label(self.main_frame, text="Check Balance", font=("Arial", 20, "bold")).pack(pady=20)
        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        def fetch_balance():
            acc_num = acc_entry.get()
            mycursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_num,))
            result = mycursor.fetchone()
            if result:
                showinfo("Balance", f"Your current balance is: ₹{result[0]}")
            else:
                showerror("Error", "Account not found!")

        Button(self.main_frame, text="Check Balance", command=fetch_balance).pack(pady=20)

    def depo_cash(self):
        self.clear_frame()
        Label(self.main_frame, text="Deposit Cash", font=("Arial", 20, "bold")).pack(pady=20)

        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        Label(self.main_frame, text="Amount:").pack()
        amt_entry = Entry(self.main_frame, width=40)
        amt_entry.pack()

        def deposit():
            acc_num = acc_entry.get()
            try:
                amount = str(amt_entry.get())
                sql = "UPDATE users SET balance = balance + %s WHERE account_number = %s"
                mycursor.execute(sql, (amount, acc_num))
                if mycursor.rowcount > 0:
                    mydb.commit()
                    showinfo("Success", "Deposit successful!")
                else:
                    showerror("Error", "Account not found!")
            except ValueError:
                showerror("Error", "Enter a valid amount!")

        Button(self.main_frame, text="Deposit", command=deposit).pack(pady=20)

    def with_cash(self):
        self.clear_frame()
        Label(self.main_frame, text="Withdraw Cash", font=("Arial", 20, "bold")).pack(pady=20)

        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        Label(self.main_frame, text="Amount:").pack()
        amt_entry = Entry(self.main_frame, width=40)
        amt_entry.pack()

        def withdraw():
            acc_num = acc_entry.get()
            try:
                amount = float(amt_entry.get())
                mycursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_num,))
                current_bal = mycursor.fetchone()
                if current_bal and current_bal[0] >= amount:
                    sql = "UPDATE users SET balance = balance - %s WHERE account_number = %s"
                    mycursor.execute(sql, (amount, acc_num))
                    mydb.commit()
                    showinfo("Success", "Withdrawal successful!")
                else:
                    showerror("Error", "Insufficient balance or invalid account!")
            except ValueError:
                showerror("Error", "Enter a valid amount!")

        Button(self.main_frame, text="Withdraw", command=withdraw).pack(pady=20)

    def update_add(self):
        self.clear_frame()
        Label(self.main_frame, text="Update Address", font=("Arial", 20, "bold")).pack(pady=20)

        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        Label(self.main_frame, text="New Address:").pack()
        addr_entry = Entry(self.main_frame, width=40)
        addr_entry.pack()

        def update():
            acc_num = acc_entry.get()
            new_addr = addr_entry.get()
            sql = "UPDATE users SET address = %s WHERE account_number = %s"
            mycursor.execute(sql, (new_addr, acc_num))
            if mycursor.rowcount > 0:
                mydb.commit()
                showinfo("Success", "Address updated successfully!")
            else:
                showerror("Error", "Account not found!")

        Button(self.main_frame, text="Update", command=update).pack(pady=20)

    def update_ph_no(self):
        self.clear_frame()
        Label(self.main_frame, text="Update Phone Number", font=("Arial", 20, "bold")).pack(pady=20)

        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        Label(self.main_frame, text="New Phone Number:").pack()
        ph_entry = Entry(self.main_frame, width=40)
        ph_entry.pack()

        def update():
            acc_num = acc_entry.get()
            new_ph = ph_entry.get()
            sql = "UPDATE users SET phone = %s WHERE account_number = %s"
            mycursor.execute(sql, (new_ph, acc_num))
            if mycursor.rowcount > 0:
                mydb.commit()
                showinfo("Success", "Phone number updated successfully!")
            else:
                showerror("Error", "Account not found!")

        Button(self.main_frame, text="Update", command=update).pack(pady=20)

    def update_all(self):
        self.clear_frame()
        Label(self.main_frame, text="Update Address & Phone", font=("Arial", 20, "bold")).pack(pady=20)

        Label(self.main_frame, text="Account Number:").pack()
        acc_entry = Entry(self.main_frame, width=40)
        acc_entry.pack()

        Label(self.main_frame, text="New Address:").pack()
        addr_entry = Entry(self.main_frame, width=40)
        addr_entry.pack()

        Label(self.main_frame, text="New Phone Number:").pack()
        ph_entry = Entry(self.main_frame, width=40)
        ph_entry.pack()

        def update():
            acc_num = acc_entry.get()
            new_addr = addr_entry.get()
            new_ph = ph_entry.get()
            sql = "UPDATE users SET address = %s, phone = %s WHERE account_number = %s"
            mycursor.execute(sql, (new_addr, new_ph, acc_num))
            if mycursor.rowcount > 0:
                mydb.commit()
                showinfo("Success", "Details updated successfully!")
            else:
                showerror("Error", "Account not found!")

        Button(self.main_frame, text="Update", command=update).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()