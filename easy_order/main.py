from database import (
    get_tables, add_table, update_table_status, clear_one_table, clear_tables,
    get_orders, add_order, update_order_status, clear_one_order, clear_orders,
    get_menu, add_menu_item, delete_menu_item,
    get_table_summary, get_total_by_table, get_total_orders
)
# ------------------- Tables Menu -------------------
def tables_menu():
    while True:
        print("\n=== TABLES MENU ===")
        print("1. Show Tables")
        print("2. Add Table")
        print("3. Update Table Status")
        print("4. Delete Table")
        print("5. Delete all Tables")
        print("6. Back to Main Menu\n")

        choice = input("Select an option: ").strip()
        print()

        match choice:
            case "1":
                tables = get_tables()
                for table in tables:
                    print(f"Table {table[0]}: {table[1]}")
                print()

            case "2":
                number = int(input("Enter table number to add: "))
                add_table(number)
                print()

            case "3":
                number = int(input("Enter table number to update: "))
                status = input("New status (Free/Occupied): ")
                update_table_status(number, status)
                print()

            case "4":
                number = int(input("Enter table number to delete: "))
                clear_one_table(number)
                print()

            case "5":
                clear_tables()

            case "6":
                break
            case _:
                print("Invalid option, try again.\n")

# ------------------- Orders Menu -------------------
def orders_menu():
    while True:
        print("\n=== ORDERS MENU ===")
        print("1. Show Orders")
        print("2. Add Order")
        print("3. Update Order Status")
        print("4. Delete one Order")
        print("5. Delete All Orders")
        print("6. Back to Main Menu\n")

        choice = input("Select an option: ").strip()
        print()

        match choice:
            case "1":
                table_input = input("Table number (leave empty for all): ")
                if table_input.strip() == "":
                    orders = get_orders()
                else:
                    orders = get_orders(int(table_input))
                for order in orders:
                    print(f"Order {order[0]} - Table {order[1]}: {order[2]} x {order[3]} ({order[4]})")
                print()

            case "2":
                menu = get_menu()
                print("\n--- Menu ---")
                for item in menu:
                    print(f"{item[0]}: {item[1]} ({item[2]}) - ${item[3]:.2f}")
                print()
                table = int(input("Enter table number: "))
                item_id = int(input("Enter menu item ID to order: "))
                quantity = int(input("Enter quantity: "))
                item = next((i for i in menu if i[0] == item_id), None)
                if item:
                    add_order(table, item[1], quantity)
                else:
                    print("Item not found.")
                print()

            case "3":
                order_id = int(input("Enter order ID to update: "))
                status = input("New order status (Pending/Served): ")
                update_order_status(order_id, status)
                print()

            case "4":
                order_id = int(input("Enter order ID to delete: "))
                clear_one_order(order_id)
                print()

            case "5":
                clear_orders()
            
            case "6":
                break
            case _:
                print("Invalid option, try again.\n")

# ------------------- Menu Items Menu -------------------
def menu_items_menu():
    while True:
        print("\n=== MENU ITEMS MENU ===")
        print("1. Show Menu")
        print("2. Add Menu Item")
        print("3. Delete Menu Item")
        print("4. Back to Main Menu\n")

        choice = input("Select an option: ").strip()
        print()

        match choice:
            case "1":
                menu = get_menu()
                print("\n--- Menu ---")
                for item in menu:
                    print(f"{item[0]}: {item[1]} ({item[2]}) - ${item[3]:.2f}")
                print()

            case "2":
                name = input("Menu item name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                add_menu_item(name, category, price)
                print()

            case "3":
                item_id = int(input("Menu item ID to delete: "))
                delete_menu_item(item_id)
                print()

            case "4":
                break
            case _:
                print("Invalid option, try again.\n")

# ------------------- Menu Items Menu -------------------
def reports_menu():
    while True:
        print("\n=== REPORTS MENU ===")
        print("1. Show Table Summary")
        print("2. Show total Orders by Item")
        print("3. Back to main Menu\n")

        choice = input("Select an option: ").strip()
        print()

        match choice:
            case "1":
                summary = get_table_summary()
                current_table = None
                for row in summary:
                    table_number, item, total_quantity = row
                    if table_number != current_table:
                        current_table = table_number
                        print(f"\n--- Table {table_number} ---")
                    print(f"{item}: {total_quantity} units")
            
            case "2":
                totals = get_total_orders()
                print("\n--- Total Orders by Item ---")
                for item, total_quantity in totals:
                    print(f"{item}: {total_quantity} units")
                    print()
            
            case "3":
                break

            case _:
                print("Invalid option, try again.\n")

# ------------------- Main Menu -------------------
def main_menu():
    while True:
        print("\n=== EASY ORDER RESTAURANT ===")
        print("1. Tables")
        print("2. Orders")
        print("3. Menu Items")
        print("4. Reports")
        print("5. Exit\n")

        choice = input("Select an option: ").strip()
        print()

        match choice:
            case "1":
                tables_menu()
            case "2":
                orders_menu()
            case "3":
                menu_items_menu()
            case "4":
                reports_menu()
            case "5":
                print("Exiting Easy Order. Goodbye!")
                break
            case _:
                print("Invalid option, try again.\n")

if __name__ == "__main__":
    main_menu()