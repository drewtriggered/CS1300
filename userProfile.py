# get user user input for profile information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))  # type conversion
hobby = input("Enter your favorite hobby: ")

# Convert names to proper title case
first_name = first_name.title()
last_name = last_name.title()

# Calculate age (current year is 2026)
current_year = 2026
age = current_year - birth_year

# Decorative border using string repetition
border = "=" * 30

# Display formatted profile card using f-strings
print(f"\n{border}")
print("        USER PROFILE")
print(border)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Favorite Hobby: {hobby}")
print(border)