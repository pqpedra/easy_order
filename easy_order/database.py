import sqlite3  # Import the sqlite3 module to work with SQLite databases

#Connect to (or create) the database
connection = sqlite3.connect("easy_order.db")
cursor = connection.cursor()                    #Create a cursor object to execute SQL commands

#Creat the tables table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,       -- Unique ID for each table
    number INTEGER NOT NULL UNIQUE,             -- Table number
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
    cursor.execute("SELECT number, status FROM tables")
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

def clear_tables():
    """Delete all rows from the tables table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tables")    #Remove all tables from table
    connection.commit()
    connection.close()
    print("All tables cleared.")

#-----------------------------------------------
#Create orders table
#-----------------------------------------------

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number INTEGER NOT NULL,
    item TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (table_number) REFERENCES tables(number)
)
""")

connection.commit()
connection.close()
print ("Orders table created sucessfully!")

def add_order(table_number, item, quantity, status="Pending"):
    """Add a new order for a table."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO orders (table_number, item, quantity, status) VALUES (?, ?, ?, ?)", (table_number, item, quantity, status)
    )
    connection.commit()
    connection.close()
    print(f"Order added: {quantity} x {item} for table {table_number}.")

def get_orders(table_number=None):
    """Return all orders, or orders for a specific table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    if table_number:
        cursor.execute(
            "SELECT id, table_number, item, quantity, status FROM orders WHERE table_number=?", (table_number,)
        )
    else:
        cursor.execute(
            "SELECT id, table_number, item, quantity, status FROM orders"
        )
    orders = cursor.fetchall()
    connection.close()
    return orders

def update_order_status(order_id, new_status):
    """Update the status of a specific order by its ID."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE orders SET status=? WHERE id=?", (new_status, order_id)
    )
    connection.commit()
    connection.close()
    print(f"Order {order_id} status updated to '{new_status}'.")

def clear_orders():
    """Delete all rows from the orders table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM orders")    #Remove all orders from table
    connection.commit()
    connection.close()
print("All orders cleared.")