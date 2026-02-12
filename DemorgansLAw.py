# Theme park ride requirement condition
height_inches = 48
age = 8

# Original condition: (at least 48 inches tall) AND (at least 8 years old OR accompanied by an adult)
def can_ride(age, height, has_adult):
    if not height >= 48 and (age < 8 and not has_adult):
        return False
    return True

print("result1:", "" or "default" or "backup")  
print("result2:", "hello" and "" and "world")
print("result3:", 0 or [] or "found" or None)
# Test cases
print("Can ride (60 inches, 10 years, no adult):", can_ride(60, 10, False))  # True
print("Can ride (60 inches, 5 years, with adult):", can_ride(60, 5, True))  # True
#advanced l