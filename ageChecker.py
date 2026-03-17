# Ask the user for their age
age = int(input("Enter your age: "))

# Validate age
if age < 0:
    print("Error: Age cannot be negative.")
else:
    # Ask if the showing is a matinee
    matinee_input = input("Is this a matinee showing (yes/no)? ").lower()

    # Convert to Boolean using a ternary operator
    is_matinee = True if matinee_input == "yes" else False

    # Determine ticket price using nested if statements
    if age < 13:  # Child
        if is_matinee:
            price = 6.00
        else:
            price = 8.00

    elif age <= 17:  # Teen
        if is_matinee:
            price = 7.00
        else:
            price = 10.00

    elif age <= 64:  # Adult
        if is_matinee:
            price = 8.00
        else:
            price = 13.00

    else:  # Senior (65+)
        if is_matinee:
            price = 6.00
        else:
            price = 7.00

    # Display the ticket price formatted to 2 decimal places
    print(f"Your movie ticket price is: ${price:.2f}")