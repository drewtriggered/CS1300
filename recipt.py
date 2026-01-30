# Receipt calculator

customer_name = input("Enter customer name: ")
quantity = int(input("Enter quantity of items: "))
price_per_item = float(input("Enter price per item: $"))

subtotal = quantity * price_per_item
tax = subtotal * 0.07
total = subtotal + tax

print("\n" + "="*30)
print("RECEIPT")
print("="*30)
print(f"Customer: {customer_name}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price_per_item:.2f}")
print("-"*30)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print("-"*30)
print(f"Total: ${total:.2f}")
print("="*30)