import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val =  ("Raju", "Siliguri")
val =  ("Dip", "kolkata")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")