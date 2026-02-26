# Ask for student information
name = input("Enter student's name: ")

score1 = float(input("Enter Exam 1 score (0-100): "))
score2 = float(input("Enter Exam 2 score (0-100): "))
score3 = float(input("Enter Exam 3 score (0-100): "))

# Calculate average
average = (score1 + score2 + score3) / 3

# Determine letter grade
if 90 <= average <= 100:
    letter = "A"
elif 87 <= average <= 89:
    letter = "A-"
elif 83 <= average <= 86:
    letter = "B+"
elif 80 <= average <= 82:
    letter = "B"
elif 77 <= average <= 79:
    letter = "B-"
elif 73 <= average <= 76:
    letter = "C+"
elif 70 <= average <= 72:
    letter = "C"
elif 67 <= average <= 69:
    letter = "C-"
elif 63 <= average <= 66:
    letter = "D+"
elif 60 <= average <= 62:
    letter = "D"
else:
    letter = "F"

# Determine academic standing
if average >= 90:
    standing = "Dean's List"
elif average >= 70:
    standing = "Good Standing"
elif average >= 60:
    standing = "Academic Probation"
else:
    standing = "Academic Suspension Warning"

# Print formatted grade report
print("\n--- Grade Report ---")
print(f"Student Name: {name}")
print(f"Exam Scores: {score1}, {score2}, {score3}")
print(f"Average Score: {average:.2f}")
print(f"Letter Grade: {letter}")
print(f"Academic Standing: {standing}")