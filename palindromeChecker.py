# Ask the user for a word
word = input("Enter a word: ")

# Normalize the word: lowercase + remove spaces
cleaned = word.replace(" ", "").lower()

# Check if it's a palindrome
is_palindrome = cleaned == cleaned[::-1]

# Display result

print(f"Original word: {word}")
print(f"Cleaned word:  {cleaned}")
print(f"Is it a palindrome? {is_palindrome}")
