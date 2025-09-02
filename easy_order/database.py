import sqlite3

DB_NAME = "easy_order.db"

def ensure_schema():
    """Create all required tables if they do not exist."""
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

    # Menu table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
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
    #Check if table already exists
    cursor.execute("SELECT number FROM tables WHERE number=?", (number,))
    if cursor.fetchone():
        print(f"Table {number} already exists!")
    else:
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

def clear_one_table(table_number):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tables WHERE number=?", (table_number,))
    table = cursor.fetchone()
    if table:
        cursor.execute("DELETE FROM tables WHERE number=?", (table_number,))
        connection.commit()
        print(f"Table {table_number} was deleted!")
    else:
        print(f"Table {table_number} does not exist.")      
    connection.close()

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
    print(f"Order added: {quantity} x {item} for Table {table_number}.")

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

def clear_one_order(order_id):
    """Delete a single order by its ID, with existence Check"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    order = cursor.fetchone()
    if order:
        cursor.execute("DELETE FROM orders WHERE id=?", (order_id,))
        connection.commit()
        print(f"Order {order_id} was deleted!")
    else:
        print(f"Order {order_id} does not exist.")      
    connection.close()

# ----------------------------
# Menu Management
# ----------------------------
connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL
)
""")
connection.commit()
connection.close()
print("Menu table created sucessfully!")

def add_menu_item(name, category, price):
    """Add new item to the menu"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO menu (name, category, price) VALUES (?, ?, ?)", (name, category, price))
    connection.commit()
    connection.close()
    print(f"Menu item '{name}' added successfully!")

def get_menu():
    """Return all items in the menu"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, category, price FROM menu")
    items = cursor.fetchall()
    connection.close()
    return items

def delete_menu_item(name, category, price):
    """Delete 1 item from the menu table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM menu WHERE name=? AND category=? AND price=?", (name, category, price))
    connection.commit()
    connection.close()
    print(f"Menu item '{name}' deleted from Menu!")

def update_menu_item(item_id, new_name, new_category, new_price):
    """"Update 1 item from the menu table by the ID"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE menu SET name=?, category=?, price=? WHERE id=?", (new_name, new_category, new_price))
    connection.commit()
    connection.close()
    print(f"Menu item '{name}' updated in Menu!")

# ----------------------------
# Reports Management
# ----------------------------

def get_total_by_table(table_number):
    """Calculate total price of all orders for a table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    #Join orders with menu to get price
    cursor.execute("""
        SELECT o.quantity, m.price FROM orders o
        JOIN menu m ON o.item = m.name
        WHERE o.table_number = ?""", (table_number,))
    rows = cursor.fetchall()
    connection.close()

    total = sum(quantity * price for quantity, price in rows)
    return total

def get_table_summary():
    """Return a summary of orders grouped by table"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT table_number, item, SUM(quantity) as total_quantity
        FROM orders
        GROUP BY table_number, item
        ORDER BY table_number
    """)
    summary = cursor.fetchall()
    connection.close()
    return summary

def get_total_orders():
    """Return total number of orders and total quantity of items"""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT item, SUM(quantity) as total_quantity
        FROM orders
        GROUP BY item
        ORDER BY total_quantity DESC
    """)
    totals = cursor.fetchall()
    connection.close()
    return totals