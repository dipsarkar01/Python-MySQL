import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE name LIKE '%raj%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)