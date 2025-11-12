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
        self.title("Dip's Notepad")

        try:
            self.iconbitmap("bank.ico")
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

        Label(self, text="Welcome to XYZ Bank", font=("Arial", 24, "bold")).pack(pady=40)
        Label(self, text="Choose an option from the menu above.", font=("Arial", 14)).pack()

    def about(self):
        showinfo(title="About", message="XYZ Bank\nVersion 1.0")

    def create_new_acc(self):
        create_new_acc_window = Toplevel(self)
        width, height = 600, 400
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        create_new_acc_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        create_new_acc_window.resizable(False, False)
        create_new_acc_window.title("Create New Account")
        Label(create_new_acc_window, text="Create New Account", font=("Arial", 20, "bold")).pack(pady=20)
        name_label = Label(create_new_acc_window, text="Name:")
        name_label.pack()
        name_entry = Entry(create_new_acc_window, width=40)
        name_entry.pack()
        addr_label = Label(create_new_acc_window, text="Address:")
        addr_label.pack()
        addr_entry = Entry(create_new_acc_window, width=40)
        addr_entry.pack()
        phone_label = Label(create_new_acc_window, text="Phone Number:")
        phone_label.pack()
        phone_entry = Entry(create_new_acc_window, width=40)
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
        Button(create_new_acc_window, text="Create Account", command=save_account).pack(pady=20)

    def check_bal(self):
        check_bal_window = Toplevel(self)
        width, height = 600, 400
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        check_bal_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        check_bal_window.resizable(False, False)
        check_bal_window.title("Check Balance")
        Label(check_bal_window, text="Check Balance", font=("Arial", 20, "bold")).pack(pady=20)

        Label(check_bal_window, text="Account Number:").pack()
        acc_entry = Entry(check_bal_window, width=40)
        acc_entry.pack()

        def fetch_balance():
            acc_num = acc_entry.get()
            mycursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_num,))
            result = mycursor.fetchone()
            if result:
                showinfo("Balance", f"Your current balance is: ₹{result[0]}")
            else:
                showerror("Error", "Account not found!")

        Button(check_bal_window, text="Check Balance", command=fetch_balance).pack(pady=20)

    def depo_cash(self):
        depo_cash_window = Toplevel(self)
        width, height = 600, 400
        sys_width = depo_cash_window.winfo_screenwidth()
        sys_height = depo_cash_window.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        depo_cash_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        depo_cash_window.resizable(False, False)
        depo_cash_window.title("Deposit Cash")
        Label(depo_cash_window, text="Deposit Cash", font=("Arial", 20, "bold")).pack(pady=20)

        Label(depo_cash_window, text="Account Number:").pack()
        acc_entry = Entry(depo_cash_window, width=40)
        acc_entry.pack()

        Label(depo_cash_window, text="Amount:").pack()
        amt_entry = Entry(depo_cash_window, width=40)
        amt_entry.pack()

        def deposit():
            acc_num = acc_entry.get()
            try:
                amount = float(amt_entry.get())
                sql = "UPDATE users SET balance = balance + %s WHERE account_number = %s"
                mycursor.execute(sql, (amount, acc_num))
                if mycursor.rowcount > 0:
                    mydb.commit()
                    showinfo("Success", "Deposit successful!")
                else:
                    showerror("Error", "Account not found!")
            except ValueError:
                showerror("Error", "Enter a valid amount!")

        Button(depo_cash_window, text="Deposit", command=deposit).pack(pady=20)

    def with_cash(self):
        with_cash_window = Toplevel(self)
        width, height = 600, 400
        sys_width = with_cash_window.winfo_screenwidth()
        sys_height = with_cash_window.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        with_cash_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        with_cash_window.resizable(False, False)
        with_cash_window.title("Withdraw Cash")
        Label(with_cash_window, text="Withdraw Cash", font=("Arial", 20, "bold")).pack(pady=20)

        Label(with_cash_window, text="Account Number:").pack()
        acc_entry = Entry(with_cash_window, width=40)
        acc_entry.pack()

        Label(with_cash_window, text="Amount:").pack()
        amt_entry = Entry(with_cash_window, width=40)
        amt_entry.pack()

        def withdraw():
            acc_num = acc_entry.get()
            try:
                amount = str(amt_entry.get())
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

        Button(with_cash_window, text="Withdraw", command=withdraw).pack(pady=20)

    def update_add(self):
        update_add_window = Toplevel(self)
        width, height = 600, 400
        sys_width = update_add_window.winfo_screenwidth()
        sys_height = update_add_window.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        update_add_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        update_add_window.resizable(False, False)
        update_add_window.title("Update Address")
        Label(update_add_window, text="Update Address", font=("Arial", 20, "bold")).pack(pady=20)

        Label(update_add_window, text="Account Number:").pack()
        acc_entry = Entry(update_add_window, width=40)
        acc_entry.pack()

        Label(update_add_window, text="New Address:").pack()
        addr_entry = Entry(update_add_window, width=40)
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

        Button(update_add_window, text="Update", command=update).pack(pady=20)
    
    def update_ph_no(self):
        update_ph_no_window = Toplevel(self)
        width, height = 600, 400
        sys_width = update_ph_no_window.winfo_screenwidth()
        sys_height = update_ph_no_window.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        update_ph_no_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        update_ph_no_window.resizable(False, False)
        update_ph_no_window.title("Update Phone Number")
        Label(update_ph_no_window, text="Update Phone Number", font=("Arial", 20, "bold")).pack(pady=20)

        Label(update_ph_no_window, text="Account Number:").pack()
        acc_entry = Entry(update_ph_no_window, width=40)
        acc_entry.pack()

        Label(update_ph_no_window, text="New Phone Number:").pack()
        ph_entry = Entry(update_ph_no_window, width=40)
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

        Button(update_ph_no_window, text="Update", command=update).pack(pady=20)

    def update_all(self):
        update_all_window = Toplevel(self)
        width, height = 600, 400
        sys_width = update_all_window.winfo_screenwidth()
        sys_height = update_all_window.winfo_screenheight()
        c_x = int(sys_width / 2 - width / 2)
        c_y = int(sys_height / 2 - height / 2)
        update_all_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        update_all_window.resizable(False, False)
        update_all_window.title("Update All")
        Label(update_all_window, text="Update Address & Phone", font=("Arial", 20, "bold")).pack(pady=20)

        Label(update_all_window, text="Account Number:").pack()
        acc_entry = Entry(update_all_window, width=40)
        acc_entry.pack()

        Label(update_all_window, text="New Address:").pack()
        addr_entry = Entry(update_all_window, width=40)
        addr_entry.pack()

        Label(update_all_window, text="New Phone Number:").pack()
        ph_entry = Entry(update_all_window, width=40)
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

        Button(update_all_window, text="Update", command=update).pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()