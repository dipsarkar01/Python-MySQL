import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE id = 4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")