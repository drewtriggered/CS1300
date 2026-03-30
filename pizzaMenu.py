# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================

# ----- Menu Data (do not modify) -----
# List of available pizza sizes
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
# Corresponding prices for each size
size_prices = [6.99, 9.99, 12.99, 16.99]

# List of available toppings
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple"]

# Price per topping
topping_price = 1.50

# ----- Order Storage -----
# Lists to store descriptions and prices of ordered pizzas
order_descriptions = []
order_prices = []

# Welcome message
print("Welcome to the CS 1300 Pizza Shop!\n")

# ============================================
# EXERCISE 5 — OUTER LOOP (wraps 1–4)
# ============================================
# Flag to control the ordering loop
ordering = True

# Main loop for ordering pizzas
while ordering:

    # ============================================
    # EXERCISE 1 — Display the size menu
    # ============================================
    # Print the header for pizza sizes
    print("=" * 30)
    print("PIZZA SIZES")
    print("=" * 30)

    # Loop through sizes and print each with price
    for i in range(len(sizes)):
        print(f"{i+1}. {sizes[i]:<15} ${size_prices[i]:>5.2f}")

    print("=" * 30)

    # ============================================
    # EXERCISE 2 — Get a valid size choice
    # ============================================
    # Loop until a valid size choice is made
    while True:
        choice = input("Pick a size (1-4): ")

        # Check if input is a digit
        if not choice.isdigit():
            print("Please enter a number!")
            continue

        choice = int(choice)

        # Check if choice is within range
        if choice < 1 or choice > 4:
            print("Choose 1-4.")
            continue

        # Store the chosen size index and base price
        size_choice = choice - 1
        base_price = size_prices[size_choice]
        break

    # ============================================
    # EXERCISE 3 — Add toppings
    # ============================================
    # List to store selected toppings for this pizza
    selected_toppings = []

    # Display available toppings
    print("\nAvailable toppings ($1.50 each):")
    for i in range(len(topping_names)):
        print(f"{i+1}. {topping_names[i]}")

    # Loop to add toppings until user says 'done'
    while True:
        choice = input("Add topping # (or 'done'): ").lower()

        # Exit if user is done
        if choice == "done":
            break

        # Check if input is a digit
        if not choice.isdigit():
            print("Invalid input!")
            continue

        choice = int(choice)

        # Check if topping number is valid
        if choice < 1 or choice > len(topping_names):
            print("Invalid topping number!")
            continue

        # Get the topping name
        topping = topping_names[choice - 1]

        # Check if topping already selected
        if topping in selected_toppings:
            print(f"Already added {topping}!")
            continue

        # Add topping and confirm
        selected_toppings.append(topping)
        print(f"✓ Added {topping}")

    # ============================================
    # EXERCISE 4 — Calculate price and store pizza
    # ============================================
    # Calculate total price for this pizza
    price = base_price + len(selected_toppings) * topping_price

    # Create description based on toppings
    if selected_toppings:
        description = sizes[size_choice] + " " + ", ".join(selected_toppings)
    else:
        description = sizes[size_choice] + " Cheese"

    # Store the pizza in order lists
    order_descriptions.append(description)
    order_prices.append(price)

    # ============================================
    # EXERCISE 5 — Ask to order another pizza
    # ============================================
    # Loop until valid response for ordering another pizza
    while True:
        again = input("Order another pizza? (yes/no): ").lower()

        # Continue ordering if yes
        if again in ["yes", "y"]:
            break
        # Stop ordering if no
        elif again in ["no", "n"]:
            ordering = False
            break
        else:
            print("Please enter yes or no.")

# ============================================
# POST-ORDER
# ============================================
# Check if any pizzas were ordered
if not order_descriptions:
    print("\nNo pizzas ordered. See you next time!")

else:

    # ============================================
    # EXERCISE 8 — Discount code
    # ============================================
    # Initialize discount and attempt counter
    discount = 0
    attempts = 0

    # Loop to enter discount code, up to 3 attempts
    while attempts < 3:
        code = input("\nEnter discount code (or 'none'): ").upper()

        # No discount if none
        if code == "NONE":
            break
        # Apply 10% discount
        elif code == "STUDENT10":
            discount = 0.10
            print("10% discount applied!")
            break
        # Apply 50% discount
        elif code == "HALFOFF":
            discount = 0.50
            print("50% discount applied!")
            break
        else:
            # Increment attempts on invalid code
            attempts += 1
            print("Invalid code!")

    # Message if max attempts reached
    if attempts == 3:
        print("No discount applied.")

    # ============================================
    # EXERCISE 6 — Print receipt
    # ============================================
    # Print receipt header
    print("\n" + "=" * 36)
    print("YOUR ORDER RECEIPT")
    print("=" * 36)

    # Initialize subtotal
    subtotal = 0

    # Loop through orders and print each item
    for i in range(len(order_descriptions)):
        print(f"{i+1}. {order_descriptions[i]}")
        print(f"${order_prices[i]:>6.2f}")
        subtotal += order_prices[i]

    # Calculate discount, tax, and total
    discount_amount = subtotal * discount
    subtotal_after_discount = subtotal - discount_amount
    tax = subtotal_after_discount * 0.07
    total = subtotal_after_discount + tax

    # Print summary
    print("-" * 36)
    print(f"Subtotal: ${subtotal:>6.2f}")
    print(f"Discount: -${discount_amount:>6.2f}")
    print(f"Tax (7%): ${tax:>6.2f}")
    print(f"Total:    ${total:>6.2f}")
    print("=" * 36)

    # ============================================
    # EXERCISE 7 — Most expensive pizza
    # ============================================
    # Initialize with first pizza
    max_price = order_prices[0]
    max_index = 0

    # Find the most expensive pizza
    for i in range(len(order_prices)):
        if order_prices[i] > max_price:
            max_price = order_prices[i]
            max_index = i

    # Print the most expensive pizza
    print(f"\nMost expensive pizza: {order_descriptions[max_index]} (${max_price:.2f})")

    # ============================================
    # EXERCISE 9 — Count pizzas by size
    # ============================================
    # Initialize count list for each size
    size_counts = [0, 0, 0, 0]

    # Count pizzas by checking size in description
    for desc in order_descriptions:
        for i in range(len(sizes)):
            if sizes[i] in desc:
                size_counts[i] += 1

    # Print counts
    print("\nPizza count by size:")
    for i in range(len(sizes)):
        print(f"{sizes[i]}: {size_counts[i]}")

# Final thank you message
print("\nThank you for your order!")