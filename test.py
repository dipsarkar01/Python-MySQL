# To display records fetched from a SQL table in a tabular format using Python, you can utilize the pandas library, which is excellent for data manipulation and presentation.
# Here's how you can achieve this:
# Connect to your SQL database: Use a suitable database connector library (e.g., mysql.connector for MySQL, psycopg2 for PostgreSQL, sqlite3 for SQLite).
# Execute your SQL query: Fetch the desired records from the table.
# Load the data into a Pandas DataFrame: This will automatically structure your data in a tabular format, complete with column headers.
# Print the DataFrame: Pandas provides a clear and readable representation of the DataFrame, resembling a table.
# Python

import pymysql
import pandas as pd

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'test'
}

try:
    # Establish a database connection
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # SQL query to fetch data
    sql_query = "SELECT * FROM users"  # Replace with your table name

    # Execute the query
    cursor.execute(sql_query)

    # Fetch all records
    records = cursor.fetchall()

    # Get column names from the cursor description
    column_names = [col[0] for col in cursor.description]

    # Create a Pandas DataFrame
    df = pd.DataFrame(records, columns=column_names)

    # Print the DataFrame
    print(df)

except pymysql.MySQLError as err:
    print(f"Database Error: {err}")

finally:
    # Close cursor and connection safely
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
        print("Database connection closed.")

# tri this concept.