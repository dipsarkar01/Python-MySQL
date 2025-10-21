import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)