import sqlite3

DB_NAME = "easy_order.db"

# ----------------------------
# Create tables
# ----------------------------
def create_tables():
    """Create tables and orders if they don't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Tables table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tables (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER NOT NULL UNIQUE,
        status TEXT NOT NULL
    )
    """)

    # Orders table
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
    print("Database and tables created successfully!")

# ----------------------------
# Tables management
# ----------------------------
def add_table(number, status="Free"):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tables (number, status) VALUES (?, ?)", (number, status))
    connection.commit()
    connection.close()
    print(f"Table {number} added with status '{status}'.")

def get_tables():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT number, status FROM tables")
    tables = cursor.fetchall()
    connection.close()
    return tables

def update_table_status(table_number, new_status):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE tables SET status = ? WHERE number = ?", (new_status, table_number))
    connection.commit()
    connection.close()
    print(f"Table {table_number} status updated to '{new_status}'.")

def clear_tables():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tables")
    connection.commit()
    connection.close()
    print("All tables cleared.")

# ----------------------------
# Orders management
# ----------------------------
def add_order(table_number, item, quantity, status="Pending"):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO orders (table_number, item, quantity, status) VALUES (?, ?, ?, ?)",
        (table_number, item, quantity, status)
    )
    connection.commit()
    connection.close()
    print(f"Order added: {quantity} x {item} for table {table_number}.")

def get_orders(table_number=None):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    if table_number:
        cursor.execute("SELECT id, table_number, item, quantity, status FROM orders WHERE table_number=?", (table_number,))
    else:
        cursor.execute("SELECT id, table_number, item, quantity, status FROM orders")
    orders = cursor.fetchall()
    connection.close()
    return orders

def update_order_status(order_id, new_status):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET status=? WHERE id=?", (new_status, order_id))
    connection.commit()
    connection.close()
    print(f"Order {order_id} status updated to '{new_status}'.")

def clear_orders():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM orders")
    connection.commit()
    connection.close()
    print("All orders cleared.")