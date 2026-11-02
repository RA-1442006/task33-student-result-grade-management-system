# Student Result & Grade Management System
# Internship Project Submission - Task 33

# List to store student records (dictionaries)
# Starting with some sample records for demonstration
students = [
    {
        "roll": "101",
        "name": "Aman Sharma",
        "class": "10-A",
        "marks": {"Math": 85.0, "Science": 90.0, "English": 78.0},
        "total": 253.0,
        "percentage": 84.33,
        "grade": "A",
        "status": "Pass"
    },
    {
        "roll": "102",
        "name": "Pooja Patel",
        "class": "10-A",
        "marks": {"Math": 95.0, "Science": 94.0, "English": 92.0},
        "total": 281.0,
        "percentage": 93.67,
        "grade": "A+",
        "status": "Pass"
    }
]

def find_student(roll_no):
    # Search student by roll number
    for student in students:
        if student["roll"].strip().lower() == roll_no.strip().lower():
            return student
    return None

def calculate_grade(percentage):
    # Determines grade and pass/fail status from percentage
    if percentage >= 90:
        return "A+", "Pass"
    elif percentage >= 80:
        return "A", "Pass"
    elif percentage >= 70:
        return "B", "Pass"
    elif percentage >= 60:
        return "C", "Pass"
    elif percentage >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"

def validate_and_calculate_result(student, show_output=True):
    marks = student.get("marks", {})
    if not marks:
        if show_output:
            print("\nNo marks recorded for this student yet. Please add marks first.")
        return False

    # Validate that all marks are strictly between 0 and 100
    for sub, score in marks.items():
        if score < 0 or score > 100:
            if show_output:
                print(f"\nError: Invalid mark ({score}) found in {sub}. Marks must be between 0 and 100.")
            return False

    total = sum(marks.values())
    percentage = round(total / len(marks), 2)
    grade, status = calculate_grade(percentage)

    student["total"] = round(total, 2)
    student["percentage"] = percentage
    student["grade"] = grade
    student["status"] = status

    if show_output:
        print("\n---------------- Result Card ----------------")
        print(f"Roll Number : {student['roll']}")
        print(f"Name        : {student['name']}")
        print(f"Class       : {student['class']}")
        print("Subjects & Marks:")
        for sub, score in marks.items():
            print(f"  - {sub:<12}: {score}")
        print(f"Total Marks : {student['total']} / {len(marks) * 100}")
        print(f"Percentage  : {student['percentage']}%")
        print(f"Grade       : {student['grade']}")
        print(f"Status      : {student['status']}")
        print("---------------------------------------------")

    return True

def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()
    if not roll:
        print("Roll number cannot be empty.")
        return

    if find_student(roll):
        print(f"Error: A student with roll number '{roll}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    std_class = input("Enter Class: ").strip()
    if not std_class:
        print("Class cannot be empty.")
        return

    new_student = {
        "roll": roll,
        "name": name,
        "class": std_class,
        "marks": {},
        "total": 0.0,
        "percentage": 0.0,
        "grade": "N/A",
        "status": "Pending"
    }
    students.append(new_student)
    print(f"Student '{name}' (Roll No: {roll}) added successfully!")

    # Prompt if user wants to add marks immediately
    add_now = input("Do you want to add subjects and marks now? (y/n): ").strip().lower()
    if add_now == "y":
        add_or_update_marks(new_student)

def add_or_update_marks(student=None):
    if student is None:
        print("\n--- Add/Update Marks ---")
        roll = input("Enter Roll Number of the student: ").strip()
        student = find_student(roll)
        if not student:
            print(f"Error: Student with roll number '{roll}' not found.")
            return

    print(f"\nEntering marks for {student['name']} (Roll: {student['roll']}, Class: {student['class']})")

    if student["marks"]:
        print("Existing marks:")
        for sub, sc in student["marks"].items():
            print(f"  {sub}: {sc}")

    while True:
        try:
            count = int(input("How many subjects do you want to enter/update? "))
            if count <= 0:
                print("Count must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

    for i in range(count):
        sub_name = input(f"\nEnter name of subject {i + 1}: ").strip()
        while not sub_name:
            print("Subject name cannot be empty.")
            sub_name = input(f"Enter name of subject {i + 1}: ").strip()

        # Validate marks input between 0 and 100
        while True:
            try:
                score = float(input(f"Enter marks for {sub_name} (0-100): "))
                if 0 <= score <= 100:
                    student["marks"][sub_name] = score
                    break
                else:
                    print("Invalid score! Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numerical value for marks.")

    # Automatically calculate total, percentage and grade
    validate_and_calculate_result(student, show_output=True)
    print("Marks updated and grade calculated successfully!")

def update_student():
    print("\n--- Update Student Details ---")
    roll = input("Enter Roll Number to update: ").strip()
    student = find_student(roll)
    if not student:
        print(f"Error: Student with roll number '{roll}' not found.")
        return

    print(f"Current Name : {student['name']}")
    print(f"Current Class: {student['class']}")
    print("(Press Enter to leave a field unchanged)")

    new_name = input("Enter new name: ").strip()
    if new_name:
        student["name"] = new_name

    new_class = input("Enter new class: ").strip()
    if new_class:
        student["class"] = new_class

    print("Student details updated successfully!")

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number of student to delete: ").strip()
    student = find_student(roll)
    if not student:
        print(f"Error: Student with roll number '{roll}' not found.")
        return

    confirm = input(f"Are you sure you want to delete {student['name']} (Roll: {student['roll']})? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")

def search_student():
    print("\n--- Search Student ---")
    print("1. Search by Roll Number")
    print("2. Search by Name")
    choice = input("Enter search option (1/2): ").strip()

    matches = []
    if choice == "1":
        roll = input("Enter Roll Number: ").strip()
        student = find_student(roll)
        if student:
            matches.append(student)
    elif choice == "2":
        query = input("Enter student name or partial name: ").strip().lower()
        if query:
            for s in students:
                if query in s["name"].lower():
                    matches.append(s)
    else:
        print("Invalid choice.")
        return

    if not matches:
        print("No matching student records found.")
        return

    print(f"\nFound {len(matches)} matching student(s):")
    for s in matches:
        print("-" * 45)
        print(f"Roll Number : {s['roll']}")
        print(f"Name        : {s['name']}")
        print(f"Class       : {s['class']}")
        if s["marks"]:
            print("Marks:")
            for sub, sc in s["marks"].items():
                print(f"  {sub:<12}: {sc}")
            print(f"Total Marks : {s['total']}")
            print(f"Percentage  : {s['percentage']}%")
            print(f"Grade       : {s['grade']}")
            print(f"Status      : {s['status']}")
        else:
            print("Marks       : No marks entered yet")
        print("-" * 45)

def view_all_students():
    print("\n--- All Students List ---")
    if not students:
        print("No student records available in the system.")
        return

    # Print a formatted table
    print("=" * 82)
    header = f"{'Roll':<8} {'Name':<20} {'Class':<10} {'Total':<10} {'Percentage':<14} {'Grade':<8} {'Status':<8}"
    print(header)
    print("-" * 82)

    for s in students:
        pct_display = f"{s['percentage']}%" if s['marks'] else "N/A"
        tot_display = str(s['total']) if s['marks'] else "N/A"
        row = f"{s['roll']:<8} {s['name']:<20} {s['class']:<10} {tot_display:<10} {pct_display:<14} {s['grade']:<8} {s['status']:<8}"
        print(row)

    print("=" * 82)
    print(f"Total Students Registered: {len(students)}")

def grade_calculation_module():
    print("\n--- Grade Calculation Module ---")
    roll = input("Enter Roll Number to calculate/view grade: ").strip()
    student = find_student(roll)
    if not student:
        print(f"Error: Student with roll number '{roll}' not found.")
        return

    if not student["marks"]:
        print("No marks recorded for this student. Please add marks first using Option 2.")
        return

    # Validate marks and compute result
    validate_and_calculate_result(student, show_output=True)

def performance_summary():
    print("\n--- Class Performance Summary ---")

    # Filter students who have evaluated marks
    evaluated = [s for s in students if s["marks"]]

    if not evaluated:
        print("No evaluated student records found to generate summary.")
        return

    total_evaluated = len(evaluated)
    percentages = [s["percentage"] for s in evaluated]
    class_average = round(sum(percentages) / total_evaluated, 2)

    highest_student = max(evaluated, key=lambda s: s["percentage"])
    lowest_student = min(evaluated, key=lambda s: s["percentage"])

    pass_count = sum(1 for s in evaluated if s["status"] == "Pass")
    fail_count = sum(1 for s in evaluated if s["status"] == "Fail")

    # Grade distribution counts
    grade_counts = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in evaluated:
        g = s["grade"]
        if g in grade_counts:
            grade_counts[g] += 1

    print(f"Total Evaluated Students : {total_evaluated}")
    print(f"Class Average Percentage : {class_average}%")
    print(f"Highest Scorer           : {highest_student['name']} ({highest_student['percentage']}%, Grade {highest_student['grade']})")
    print(f"Lowest Scorer            : {lowest_student['name']} ({lowest_student['percentage']}%, Grade {lowest_student['grade']})")
    print(f"Passed Students Count    : {pass_count}")
    print(f"Failed Students Count    : {fail_count}")
    print("\nGrade Distribution:")
    for grade, count in grade_counts.items():
        print(f"  Grade {grade:<2} : {count} student(s)")
    print("---------------------------------")

def show_menu():
    print("\n==========================================")
    print(" STUDENT RESULT & GRADE MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Add Student")
    print("2. Add/Update Subjects and Marks")
    print("3. Update Student Details")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. View All Students")
    print("7. Grade Calculation Module")
    print("8. Performance Summary")
    print("9. Exit")
    print("==========================================")

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_or_update_marks()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            view_all_students()
        elif choice == "7":
            grade_calculation_module()
        elif choice == "8":
            performance_summary()
        elif choice == "9":
            print("\nThank you for using Student Result & Grade Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
