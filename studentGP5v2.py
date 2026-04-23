"""
Student Grade Tracker
A modular program that collects exam scores, calculates
an average, determines a letter grade and academic standing,
and displays a formatted report.
"""


def get_student_name():
    """Prompt for and return the student's name."""
    return input("Student name: ")


def is_valid_score(score):
    """
    Check whether a score is valid.

    Args:
        score (int): The exam score to validate.

    Returns:
        bool: True if score is between 0 and 100, otherwise False.
    """
    return 0 <= score <= 100


def get_exam_scores(num_exams):
    """
    Collect exam scores with validation.

    Args:
        num_exams (int): Number of exam scores to collect.

    Returns:
        list: A list of valid integer exam scores.
    """
    scores = []

    for i in range(num_exams):
        while True:
            try:
                score = int(input(f"Exam {i + 1} score: "))
                if is_valid_score(score):
                    scores.append(score)
                    break
                else:
                    print("Invalid! Score must be between 0 and 100.")
            except ValueError:
                print("Invalid! Please enter a whole number.")

    return scores


def calculate_average(scores):
    """
    Calculate the average of a list of scores.

    Args:
        scores (list): A list of numeric scores.

    Returns:
        float: The average score.
    """
    return sum(scores) / len(scores)


def determine_results(average):
    """
    Determine the student's letter grade and academic standing.

    Args:
        average (float): The student's average score.

    Returns:
        tuple: (letter_grade, standing)
    """
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    if average >= 90:
        standing = "Dean's List"
    elif average >= 70:
        standing = "Good Standing"
    elif average >= 60:
        standing = "Academic Probation"
    else:
        standing = "Academic Warning"

    return grade, standing


def display_report(name, scores, average, grade, standing):
    """
    Display the formatted student grade report.

    Args:
        name (str): Student name.
        scores (list): List of exam scores.
        average (float): Average score.
        grade (str): Letter grade.
        standing (str): Academic standing.
    """
    print("=" * 30)
    print("STUDENT GRADE REPORT")
    print("=" * 30)

    print(f"Student: {name}")
    for i, score in enumerate(scores, start=1):
        print(f"Exam {i}: {score}")

    print("-" * 30)
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print("=" * 30)


def main():
    """Run the Student Grade Tracker program."""
    name = get_student_name()
    scores = get_exam_scores(3)
    average = calculate_average(scores)
    grade, standing = determine_results(average)
    display_report(name, scores, average, grade, standing)


main()