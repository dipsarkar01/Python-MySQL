import mysql.connector

# Connect to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",      # Change if your MySQL is on another host
    user="root",           # Your MySQL username
    password="root",       # Your MySQL password
    database="test"  # Make sure this database exists
)
# Create a cursor object
mycursor = mydb.cursor()

# Create a table (if it doesn't already exist)
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        Id INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Address VARCHAR(255)
    )
""")
print("Table 'customers' created successfully (if it didn't exist already).")