# Ask the user for three integer values
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
c = int(input("Enter integer c: "))

# Evaluate expressions
expr1 = a < b < c                          # Chained comparison
expr2 = not (a > b or b > c)               # De Morgan's candidate
expr3 = a <= b and b <= c                  # Equivalent to De Morgan's result?

# Print results
print("\nResults:")
print("a < b < c:", expr1)
print("not (a > b or b > c):", expr2)
print("a <= b and b <= c:", expr3)

# Check if second and third expressions match
print("\nDo the second and third expressions match?")
print(expr2 == expr3)