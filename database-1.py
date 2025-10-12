import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dip_db"
)
mycursor=mydb.cursor()

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS cust (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
    )
""")
print("Table 'cust' created successfully (if it didn't exist already).")

name = input("Enter your name:- ")
address = input("Enter your address:- ")

sql = "INSERT INTO cust (name, address) VALUES (%s, %s)"
val =  (name,address)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")