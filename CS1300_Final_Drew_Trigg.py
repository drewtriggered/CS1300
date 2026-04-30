# FizzBuzz program
for i in range(1, 31):
    # print Fizz for multiples of 3, Buzz for multiples of 5,
    # and FizzBuzz for multiples of both
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# ----------------------------
# Times Table Program
n = 6
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # print each product in a formatted grid
        print(f"{i * j:4}", end="")
    print()

# ----------------------------
# Remove Duplicates Preserve Order
def unique_preserve_order(items):
    unique = []
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
            unique.append(item)
    return unique

# ----------------------------
# Fibonacci Sequence Program
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(f"First 20 Fibonacci numbers: {fibonacci(20)}")

# ----------------------------
# Mini Banking System
balance = 1000.0
history = []

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show transaction history")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print(f"Current balance: ${balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                history.append(f"Deposit: +${amount:.2f}")
                print("Deposit successful.")
            else:
                print("Amount must be positive.")
        except:
            print("Invalid input.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                history.append(f"Withdraw: -${amount:.2f}")
                print("Withdrawal successful.")
        except:
            print("Invalid input.")

    elif choice == "4":
        if history:
            print("\nTransaction History:")
            for transaction in history:
                print(transaction)
        else:
            print("No transactions yet.")

    elif choice == "5":
        print(f"Final balance: ${balance:.2f}")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")