# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Total number of characters (including spaces)
total_chars = len(sentence)

# Total number of characters (excluding spaces)
chars_no_spaces = len(sentence.replace(" ", ""))

# Number of words
words = len(sentence.split())

# Number of vowels (case insensitive)
vowels = "aeiou"
vowel_count = sum(1 for ch in sentence.lower() if ch in vowels)

# Uppercase version
upper_sentence = sentence.upper()

# Lowercase version
lower_sentence = sentence.lower()

# Reversed sentence
reversed_sentence = sentence[::-1]

# Starts with a capital letter?
starts_with_capital = sentence[0].isupper() if sentence else False

# Ends with proper punctuation
proper_punctuation = sentence.endswith((".", "!", "?"))

# Decorative border using string repetition
border = "-" * 40

# Display results
print(f"\n{border}")
print("          SENTENCE ANALYSIS")
print(f"{border}")
print(f"Total characters (with spaces): {total_chars}")
print(f"Total characters (no spaces):   {chars_no_spaces}")
print(f"Number of words:                {words}")
print(f"Number of vowels:               {vowel_count}")
print(f"Uppercase:                      {upper_sentence}")
print(f"Lowercase:                      {lower_sentence}")
print(f"Reversed:                       {reversed_sentence}")
print(f"Starts with capital letter:     {starts_with_capital}")
print(f"Ends with proper punctuation:   {proper_punctuation}")
print(border)