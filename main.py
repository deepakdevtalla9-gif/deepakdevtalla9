"""Student Record Management System using CSV or JSON storage."""

import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
FIELDS = ["student_id", "name", "course", "marks"]


def get_storage_path(storage_format):
    """Return the data file path for the chosen format."""
    if storage_format == "csv":
        return DATA_DIR / "students.csv"
    return DATA_DIR / "students.json"


def load_students(path, storage_format):
    """Load records. Return an empty list if the file does not exist yet."""
    if not path.exists():
        return []
    try:
        if storage_format == "csv":
            with path.open("r", newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError, csv.Error) as error:
        print(f"Could not read data file: {error}")
        return []


def save_students(path, storage_format, students):
    """Save all records to CSV or JSON."""
    try:
        if storage_format == "csv":
            with path.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(students)
        else:
            with path.open("w", encoding="utf-8") as file:
                json.dump(students, file, indent=4)
        return True
    except (OSError, csv.Error, TypeError) as error:
        print(f"Could not save data: {error}")
        return False


def find_student(students, student_id):
    """Return a matching student dictionary, or None."""
    return next((s for s in students if s["student_id"] == student_id), None)


def add_student(students):
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("That student ID already exists.")
        return

    name = input("Student name: ").strip()
    course = input("Course: ").strip()
    try:
        marks = float(input("Marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Marks must be a number.")
        return

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    students.append({
        "student_id": student_id,
        "name": name,
        "course": course,
        "marks": str(marks)
    })
    print("Student added.")


def view_students(students):
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student.get('student_id', '')} | "
            f"Name: {student.get('name', '')} | "
            f"Course: {student.get('course', '')} | "
            f"Marks: {student.get('marks', '')}"
        )


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)
    if student:
        print("Found:", student)
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    marks_text = input(f"Marks [{student['marks']}]: ").strip()

    if name:
        student["name"] = name
    if course:
        student["course"] = course
    if marks_text:
        try:
            marks = float(marks_text)
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100. Marks unchanged.")
            else:
                student["marks"] = str(marks)
        except ValueError:
            print("Invalid marks. Marks unchanged.")
    print("Update completed.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return
    confirm = input(f"Delete {student['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        print("Student deleted.")
    else:
        print("Delete cancelled.")


def choose_format():
    while True:
        choice = input("Choose storage format (csv/json): ").strip().lower()
        if choice in ("csv", "json"):
            return choice
        print("Please type csv or json.")


def main():
    print("=== Student Record Management System ===")
    storage_format = choose_format()
    path = get_storage_path(storage_format)
    students = load_students(path, storage_format)

    actions = {
        "1": ("Add student", add_student),
        "2": ("View all students", view_students),
        "3": ("Search student", search_student),
        "4": ("Update student", update_student),
        "5": ("Delete student", delete_student),
    }

    while True:
        print("\n1. Add student\n2. View all students\n3. Search student")
        print("4. Update student\n5. Delete student\n6. Save and exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            if save_students(path, storage_format, students):
                print(f"Records saved to: {path}")
            break
        if choice in actions:
            actions[choice][1](students)
            # Save after each operation so changes are not lost on exit.
            save_students(path, storage_format, students)
        else:
            print("Invalid option. Choose a number from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped safely.")
