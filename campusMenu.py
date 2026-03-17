# Display menu
print("Campus Café Menu")
print("1. Coffee - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad - $5.50")
print("4. Combo (Sandwich + Coffee) - $8.00")
print("5. Exit")

choice = input("Enter your choice (1-5): ")

price = 0
item_name = ""

# ---- Menu Logic ----
if choice == "1":  # Coffee
    item_name = "Coffee"
    size = input("Choose size (small/medium/large): ").lower()

    if size == "medium":
        price = 4.50
    elif size == "large":
        price = 5.50
    elif size == "small":
        price = 3.50
    else:
        print("Invalid size. Defaulting to Small.")
        size = "small"
        price = 3.50

    item_name += f" ({size.capitalize()})"

elif choice == "2":  # Sandwich
    item_name = "Sandwich"
    price = 6.00
    cheese = input("Add cheese? (yes/no): ").lower()

    if cheese == "yes":
        price += 0.75
        item_name += " + Cheese"

elif choice == "3":  # Salad
    item_name = "Salad"
    price = 5.50
    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").lower()

    if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
        print("Invalid dressing. Defaulting to none.")
        dressing = "none"

    item_name += f" ({dressing.capitalize()} dressing)"

elif choice == "4":  # Combo
    item_name = "Combo"
    price = 8.00

    # Coffee size
    size = input("Choose coffee size (small/medium/large): ").lower()
    if size == "medium":
        price += 1.00
    elif size == "large":
        price += 2.00
    elif size != "small":
        print("Invalid size. Defaulting to Small.")
        size = "small"

    # Cheese option
    cheese = input("Add cheese to sandwich? (yes/no): ").lower()
    if cheese == "yes":
        price += 0.75

    item_name += f" (Coffee: {size.capitalize()})"

elif choice == "5":
    print("Thank you! Goodbye.")
    exit()

else:
    print("Invalid menu choice.")
    exit()

# ---- Student Name Validation ----
name = input("Enter student's name: ").strip()
while name == "":
    print("Name cannot be empty.")
    name = input("Enter student's name: ").strip()

# ---- Quantity Validation ----
try:
    quantity = int(input("Enter quantity: "))
    if quantity <= 0:
        print("Quantity must be positive.")
        exit()
except ValueError:
    print("Invalid quantity. Must be a number.")
    exit()

# ---- Calculate totals ----
subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax

# ---- Print Receipt ----
print("\n----- Campus Café Receipt -----")
print(f"Student: {name}")
print(f"Item: {item_name}")
print(f"Unit Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("-------------------------------")