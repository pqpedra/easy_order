from database import add_table, get_tables, update_table_status

# Add some tables
add_table(1)
add_table(2)
add_table(3)

# Show all tables
tables = get_tables()
print("Current tables:")
for t in tables:
    print(t)

# Update table 2 status to "Occupied"
update_table_status(2, "Occupied")

# Show updated tables
tables = get_tables()
print("Updated tables:")
for t in tables:
    print(t)