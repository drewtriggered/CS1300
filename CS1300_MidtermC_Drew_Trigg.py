# Program 1: Distance Converter
def distance_converter():
    # Get user input for distance and unit
    distance = float(input("Enter the distance value: "))
    unit = input("Enter the unit (km for kilometers, mi for miles): ").lower()
    # Convert distance based on unit and print result
    if unit == "km":
        result = distance * 0.621371
        print(f"{distance} km = {result:.2f} mi")
    elif unit == "mi":
        result = distance * 1.60934
        print(f"{distance} mi = {result:.2f} km")
    else:
        print("Invalid unit. Please enter 'km' or 'mi'.")

distance_converter()

# Program 2: Sentence Analysis
def sentence_analyzer():
    # Get multi-word sentence from user
    sentence = input("Enter a multi-word sentence: ")
    
    # Count total characters (with spaces)
    total_chars = len(sentence)
    
    # Count total words (split by spaces)
    words = sentence.split()
    total_words = len(words)
    
    # Count vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in sentence if char in vowels)
    consonant_count = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Find longest word
    longest_word = words[0] if words else ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    # Print analysis results
    print(f"Total characters (with spaces): {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")
    print(f"Average word length: {avg_word_length:.2f}")
    print(f"Longest word: {longest_word}")

sentence_analyzer()

# Program 3: Gradebook Manager
def gradebook_manager():
    # Initialize parallel lists
    assignments = ["Quiz 1", "Homework 1", "Lab 1", "Quiz 2", "Homework 2"]
    scores = [85, 92, 78, 88, 95]
    
    # Print original gradebook
    print("\n--- Original Gradebook ---")
    print(f"{'Assignment':<15} {'Score':<10}")
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} {scores[i]:<10}")
    
    # Find highest and lowest scoring assignments
    highest_idx = 0
    lowest_idx = 0
    for i in range(len(scores)):
        if scores[i] > scores[highest_idx]:
            highest_idx = i
        if scores[i] < scores[lowest_idx]:
            lowest_idx = i
    print(f"\nHighest score: {assignments[highest_idx]} ({scores[highest_idx]})")
    print(f"Lowest score: {assignments[lowest_idx]} ({scores[lowest_idx]})")
    
    # Calculate overall average
    total = sum(scores)
    average = total / len(scores)
    print(f"Overall average: {average:.2f}")
    
    # Assign letter grades
    print("\nLetter Grades:")
    for i in range(len(assignments)):
        if scores[i] >= 90:
            grade = "A"
        elif scores[i] >= 80:
            grade = "B"
        elif scores[i] >= 70:
            grade = "C"
        elif scores[i] >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"{assignments[i]}: {grade}")
    
    # Append new assignment
    assignments.append("Lab 2")
    scores.append(90)
    print("\nAfter appending Lab 2 with score 90:")
    print(f"{'Assignment':<15} {'Score':<10}")
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} {scores[i]:<10}")
    
    # Remove Quiz 1
    quiz1_idx = assignments.index("Quiz 1")
    assignments.pop(quiz1_idx)
    scores.pop(quiz1_idx)
    print("\nAfter removing Quiz 1:")
    print(f"{'Assignment':<15} {'Score':<10}")
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} {scores[i]:<10}")
    
    # Pop last assignment
    removed_assignment = assignments.pop()
    removed_score = scores.pop()
    print(f"\nPopped: {removed_assignment} with score {removed_score}")
    
    # Print final gradebook and length
    print("\nFinal Gradebook:")
    print(f"{'Assignment':<15} {'Score':<10}")
    for i in range(len(assignments)):
        print(f"{assignments[i]:<15} {scores[i]:<10}")
    print(f"Total assignments: {len(assignments)}")

gradebook_manager()