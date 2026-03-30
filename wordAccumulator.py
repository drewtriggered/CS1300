# Given a list of words, find:
# 1. The total number of characters across all words (accumulator)
# 2. How many words have more than 4 characters (counter)
# 3. Stop processing if you encounter the word "STOP" (sentinel)
words = ["cat", "elephant", "dog", "python", "STOP", "rhinoceros", "bat"]
total_chars = 0
long_count = 0
for word in words:
    if word == "STOP": #This is the Sentinel
        break
    total_chars += len(word)  # This is the Accumulator for total characters
    if len(word) > 4:
        long_count += 1  # This is the Counter for words longer than 4 characters
print(f"Total characters: {total_chars}")
print(f"Words longer than 4 chars: {long_count}")
# Expected: Total characters: 24, long_count: 2
# Used all three patterns together
