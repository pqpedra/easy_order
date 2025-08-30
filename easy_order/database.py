import sqlite3  # Import the sqlite3 module to work with SQLite databases

#Connect to (or create) the database
connection = sqlite3.connect("easy_order.db")
cursor = connection.cursor()                    #Create a cursor object to execute SQL commands

#Creat the tables table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,       -- Unique ID for each table
    number INTEGER NOT NULL,                    -- Table number
    status TEXT NOT NULL                        -- Status: "Free" or "Occupied"
)
""")

#Save changes and close the connection
connection.commit()     #Commit the changes to the database
connection.close()      #Close the connection to free resources

print("Databse and tables created sucessfully!")

DB_NAME = "easy_order.db"       #Database file

#-----------------------------------------------
#Functions to manage tables
#-----------------------------------------------

def add_table(number, status = "Free"):
    """Add a new table with a number and status"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tables (number, status) VALUES (?, ?)", (number, status))
    connection.commit()
    connection.close()
    print (f"Table {number} added with status '{status}'.")

def get_tables():
    """Return all tables and their status"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT id, number, status FROM tables")
    tables = cursor.fetchall()
    connection.close()
    return tables

def update_table_status(table_number, new_status):
    """Update the status of a tbale by its number."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE tables SET status = ? WHERE number = ?", (new_status, table_number))
    connection.commit()
    connection.close()
    print(f"Table {table_number} status updated to '{new_status}'.")

#-----------------------------------------------
#Create orders table
#-----------------------------------------------
