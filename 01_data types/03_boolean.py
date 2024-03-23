# Demonstrating boolean truthy and false values

# Truthy values
truthy_values = [True, 1, 2.5, "Hello", [1, 2, 3], (4, 5, 6), {"name": "John"}, {1, 2, 3}]

# False values
false_values = [False, 0, 0.0, "", [], (), {}, set()]

# Printing truthy values
print("Truthy values:")
for value in truthy_values:
    print(f"{value} is {bool(value)}")

# Printing false values
print("\nFalse values:")
for value in false_values:
    print(f"{value} is {bool(value)}")