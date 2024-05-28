# I make a very simple script just to see if the data is stored and everything woks
import sqlite3

# Connect to the database
conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

# Query the passwords table
cursor.execute("SELECT * FROM passwords")

# Fetch all the rows
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the connection
conn.close()