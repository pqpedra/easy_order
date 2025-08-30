from database import add_table, get_tables, update_table_status, clear_tables
from database import add_order, get_orders, update_order_status, clear_orders

# ----------------------------
# Test tables
# ----------------------------

# Add some tables
clear_tables()
clear_orders()

add_table(1)
add_table(2)
add_table(3)

# Show current tables
print("\nCurrent tables:")
tables = get_tables()
for t in tables:
    print(t)

# Update table 2 status to "Occupied"
update_table_status(2, "Occupied")

# Show updated tables
print("\nUpdated tables:")
tables = get_tables()
for t in tables:
    print(t)


# ----------------------------
# Test orders
# ----------------------------

# Add some orders
add_order(1, "Pizza Margherita", 2)
add_order(2, "Spaghetti Carbonara", 1)
add_order(2, "Coke", 2)

# Show all orders
print("\nAll orders:")
orders = get_orders()
for o in orders:
    print(o)

# Show orders for table 2 only
print("\nOrders for table 2:")
orders_table2 = get_orders(2)
for o in orders_table2:
    print(o)

# Update order status
update_order_status(2, "Served")  # Mark second order as served

# Show updated orders
print("\nUpdated orders:")
orders = get_orders()
for o in orders:
    print(o)

