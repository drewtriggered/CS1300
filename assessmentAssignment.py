# CS 1300 - Lists Part II
# Solutions for Unit 1, Unit 2, and Unit 3 exercises

# ============================================================

print("==================================================")
print("UNIT 1: TUPLES")
print("==================================================")

# ----------------------------
print("\n--- Unit 1: Beginner Exercise ---")

rgb_color = (255, 128, 0)

print("Red:", rgb_color[0])
print("Green:", rgb_color[1])
print("Blue:", rgb_color[2])

palette = []
palette.append(rgb_color)

print("Palette:", palette)

# ----------------------------
print("\n--- Unit 1: Intermediate Exercise ---")

student1 = ("Alice", 92, 19)
student2 = ("Bob", 85, 20)
student3 = ("Charlie", 88, 18)

classroom = [student1, student2, student3]

print("Second student's name:", classroom[1][0])

name, grade, age = classroom[0]
print(f"{name} is {age} years old and has a grade of {grade}.")

# ----------------------------
print("\n--- Unit 1: Advanced Exercise ---")

original_student = ("Drew", [88, 91, 84], 0)

print("Original tuple before update:", original_student)

# Add fourth exam score to the list inside the tuple
original_student[1].append(95)

# Calculate new average
new_average = sum(original_student[1]) / len(original_student[1])

# Create a new tuple with updated final grade
updated_student = (original_student[0], original_student[1], new_average)

print("Original tuple after adding exam 4:", original_student)
print("Updated tuple with final grade:", updated_student)


# ============================================================

print("\n==================================================")
print("UNIT 2: LIST VS TUPLE COMPARISON")
print("==================================================")

# ----------------------------

print("\n--- Unit 2: Beginner Exercise ---")

homework_grades = [82, 90, 87]
today_date = (4, 23, 2026)

def boost_grades(grades):
    for i in range(len(grades)):
        grades[i] += 5

boost_grades(homework_grades)

print("Boosted homework grades:", homework_grades)
print("Today's date:", today_date)

# We used a list for grades because grades can change.
# We used a tuple for the date because a date is fixed data.

# ----------------------------
print("\n--- Unit 2: Intermediate Exercise ---")

def find_range(*args):
    return (min(args), max(args))

print("Range with 3 numbers:", find_range(10, 25, 7))
print("Range with 7 numbers:", find_range(4, 18, 2, 39, 15, 27, 9))

test_scores = [78, 92, 85, 88, 91]
print("Range from unpacked list:", find_range(*test_scores))

#=---------------------------
print("\n--- Unit 2: Advanced Exercise ---")

def calculate_statistics(*args):
    count = len(args)
    total = sum(args)
    average = total / count if count > 0 else 0
    return (count, total, average)

def update_student_records(student_records, bonus):
    updated_records = []
    for name, grade in student_records:
        updated_records.append((name, grade + bonus))
    return updated_records

student_records = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

updated_records = update_student_records(student_records, 5)

print("Original records:", student_records)
print("Updated records:", updated_records)

grades_only = [grade for name, grade in updated_records]
stats = calculate_statistics(*grades_only)

print("Statistics for updated grades:")
print("Count:", stats[0])
print("Sum:", stats[1])
print("Average:", stats[2])


# ============================================================
print("\n--- Unit 3: Beginner Exercise ---")

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Entire grid:", grid)
print("Center number:", grid[1][1])

print("Grid rows:")
for row in grid:
    for value in row:
        print(value, end=" ")
    print()

# ----------------------------
# Intermediate Exercise
# ----------------------------
print("\n--- Unit 3: Intermediate Exercise ---")

scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [score for score in scores if score >= 60]

letter_grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D"
    for score in passing_grades
]

print("Passing grades:", passing_grades)
print("Letter grades:", letter_grades)

# ----------------------------
# Advanced Exercise
# ----------------------------
print("\n--- Unit 3: Advanced Exercise ---")

multiplication_table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

print("4x4 Multiplication Table:")
for row in multiplication_table:
    for value in row:
        print(f"{value:3}", end=" ")
    print()

def sum_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

diagonal_sum = sum_diagonal(multiplication_table)
print("Sum of diagonal elements:", diagonal_sum)

even_numbers = (
    value
    for row in multiplication_table
    for value in row
    if value % 2 == 0
)

print("First 5 even numbers from the multiplication table:")
count = 0
for num in even_numbers:
    print(num, end=" ")
    count += 1
    if count == 5:
        break
print()