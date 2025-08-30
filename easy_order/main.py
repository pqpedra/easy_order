from database import (
    add_table, get_tables, update_table_status,
    add_order, get_orders, update_order_status,
    clear_tables, clear_orders, create_tables,
)

#initialize database and clean tables/orders for testing
create_tables()
clear_tables()
clear_orders()

#Pre-fill some tables
for num in range(1, 4):
    add_table(num)

# ---------------------------------------
# Helper Functions
# ---------------------------------------

def show_tables():
    tables = get_tables()
    print("\nCurrent tables:")
    for t in tables:
        print(f"Table {t[0]} - Status: {t[1]}")

def show_orders(table_number=None):
    orders = get_orders(table_number)
    if not orders:
        print("No orders found.")
        return
    print("\nOrders:")
    for o in orders:
        print(f"Order {o[0]} - Table {o[1]} - {o[2]} x{o[3]} - Status: {o[4]}")

# --------------------------------------
# Main interactive menu
# --------------------------------------

def main_menu():
    while True:
        print("\n--- Easy Order Menu ---")
        print("1. Show tables")
        print("2. Add table")
        print("3. Update table status")
        print("4. Add order")
        print("5. Update order status")
        print("6. Show orders")
        print("7. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            show_tables()
        elif choice == "2":
            number = int(input("Table number to add: "))
            add_table(number)
        elif choice == "3":
            number = int(input("Table number to update: "))
            status = input("New status (Free/Occupied): ")
            update_table_status(number, status)
        elif choice == "4":
            table = int(input("Table number: "))
            item = input("Item name: ")
            quantity = int(input("Quantity: "))
            add_order(table, item, quantity)
        elif choice == "5":
            order_id = int(input("Order ID to update: "))
            status = input("New order status (Pending/Served): ")
            update_order_status(order_id, status)
        elif choice == "6":
            table_input = input("Table number (leave empty for all tables): ")
            if table_input.strip() == "":
                show_orders()
            else:
                show_orders(int(table_input))
        elif choice == "7":
            print("Exiting Easy Order. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main_menu()