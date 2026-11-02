# Student Result & Grade Management System

**Internship Project Submission — Task 33**

A menu-driven command-line Python application developed to manage student records, validate marks, calculate grades, and generate class performance statistics.

---

## Project Overview

This project was built as part of the Python Internship (Task 33). The goal is to provide a simple, clean, and reliable console application for teachers or school administrators to record students, assign and update subject marks, compute grades automatically, and analyze the overall class performance.

The application uses core Python data structures—lists and dictionaries—to store and organize student information in memory without needing any external libraries or complex database setups.

---

## Key Features

1. **Add Student**: Registers a new student with a unique roll number, full name, and class. Validates against duplicate roll numbers and empty fields.
2. **Add / Update Marks**: Enter marks for any number of subjects. Input is strictly validated between 0 and 100 before computing results.
3. **Update Student Details**: Edit a student's name or class while keeping their existing marks and roll number intact.
4. **Delete Student**: Remove a student record from the system with a confirmation check.
5. **Search Student**: Find student records quickly using either roll number (exact match) or student name (supports partial/case-insensitive searches).
6. **View All Students**: Displays a clean, formatted table listing roll number, name, class, total marks, percentage, grade, and pass/fail status for all enrolled students.
7. **Grade Calculation Module**: Validates marks (0–100) before processing, and automatically computes total marks, percentage, letter grade, and pass/fail status.
8. **Class Performance Summary**: Computes and displays:
   - Total number of evaluated students
   - Class average percentage
   - Highest scorer details (name, percentage, grade)
   - Lowest scorer details (name, percentage, grade)
   - Passed and failed student counts
   - Grade distribution breakdown (A+, A, B, C, D, F)
9. **Exit**: Gracefully exits the program with a polite exit message.

---

## Python Concepts Demonstrated

- **Variables & Data Types**: Strings, integers, floats, booleans, lists, and dictionaries.
- **Data Structures**:
  - `list` of `dict` objects to represent the collection of students.
  - Nested `dict` to store dynamic subject names and their corresponding marks (`{"Math": 85.0, ...}`).
- **Control Flow**: `if-elif-else` conditional branches for grading boundaries, input validation, and menu selection.
- **Loops**: `while` loops for continuous menu navigation and robust input retries; `for` loops to iterate through student records, calculate totals, and print table rows.
- **Functions & Modularity**: Separate, well-scoped functions for each operation (`add_student`, `add_or_update_marks`, `calculate_grade`, `view_all_students`, etc.).
- **Input Validation & Error Handling**: `try...except ValueError` blocks paired with validation loops to catch non-numeric entries or out-of-range marks (0 to 100).
- **Formatted Output**: Standard f-string formatting for neat tabular alignment and report cards.

---

## Grading Scheme

Grades and pass/fail statuses are determined based on the student's average percentage across all entered subjects:

| Percentage Range | Grade | Status |
| :--- | :---: | :---: |
| 90% to 100% | **A+** | Pass |
| 80% to 89.99% | **A** | Pass |
| 70% to 79.99% | **B** | Pass |
| 60% to 69.99% | **C** | Pass |
| 40% to 59.99% | **D** | Pass |
| Below 40% | **F** | Fail |

*Note: Marks for every individual subject are verified to be between 0 and 100 before any calculation takes place.*

---

## Project Structure

```text
task33-student-result-grade-management-system/
├── .gitignore               # Standard Python gitignore
├── main.py                  # Main application source code
├── README.md                # Project documentation and guide
├── requirements.txt         # Dependencies note (Standard Library only)
├── sample_output.txt        # Full recorded terminal session output
└── screenshots/             # Folder for application execution screenshots
    └── README.md            # Guidelines on screenshots to capture
```

---

## How to Run

### Prerequisites
- Python 3.7 or higher installed on your system.
- No external packages or `pip install` commands required.

### Steps to Run
1. Open a terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd task33-student-result-grade-management-system
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen numbered menu prompts (1–9).

---

## Sample Usage Walkthrough

### 1. Adding a Student and Entering Marks
```text
==========================================
 STUDENT RESULT & GRADE MANAGEMENT SYSTEM
==========================================
1. Add Student
2. Add/Update Subjects and Marks
3. Update Student Details
4. Delete Student
5. Search Student
6. View All Students
7. Grade Calculation Module
8. Performance Summary
9. Exit
==========================================
Enter choice (1-9): 1

--- Add New Student ---
Enter Roll Number: 103
Enter Student Name: Rohan Gupta
Enter Class: 10-A
Student 'Rohan Gupta' (Roll No: 103) added successfully!
Do you want to add subjects and marks now? (y/n): y

Entering marks for Rohan Gupta (Roll: 103, Class: 10-A)
How many subjects do you want to enter/update? 3

Enter name of subject 1: Math
Enter marks for Math (0-100): 76

Enter name of subject 2: Science
Enter marks for Science (0-100): 82

Enter name of subject 3: English
Enter marks for English (0-100): 68

---------------- Result Card ----------------
Roll Number : 103
Name        : Rohan Gupta
Class       : 10-A
Subjects & Marks:
  - Math        : 76.0
  - Science     : 82.0
  - English     : 68.0
Total Marks : 226.0 / 300
Percentage  : 75.33%
Grade       : B
Status      : Pass
---------------------------------------------
Marks updated and grade calculated successfully!
```

### 2. Viewing All Students
```text
--- All Students List ---
==================================================================================
Roll     Name                 Class      Total      Percentage     Grade    Status  
----------------------------------------------------------------------------------
101      Aman Sharma          10-A       253.0      84.33%         A        Pass    
102      Pooja Patel          10-A       281.0      93.67%         A+       Pass    
103      Rohan Gupta          10-A       226.0      75.33%         B        Pass    
==================================================================================
Total Students Registered: 3
```

### 3. Class Performance Summary
```text
--- Class Performance Summary ---
Total Evaluated Students : 3
Class Average Percentage : 84.44%
Highest Scorer           : Pooja Patel (93.67%, Grade A+)
Lowest Scorer            : Rohan Gupta (75.33%, Grade B)
Passed Students Count    : 3
Failed Students Count    : 0

Grade Distribution:
  Grade A+ : 1 student(s)
  Grade A  : 1 student(s)
  Grade B  : 1 student(s)
  Grade C  : 0 student(s)
  Grade D  : 0 student(s)
  Grade F  : 0 student(s)
---------------------------------
```

*(For full transcripts of search, grade calculation, and exit, see `sample_output.txt`)*

---

## Approach & Design Decisions

1. **Separation of Concerns**: Each menu option maps to an independent function. Common operations (such as finding a student by roll number or calculating grades) are factored into reusable helper routines (`find_student`, `calculate_grade`, `validate_and_calculate_result`).
2. **Robust Input Validation**: Bad input will not crash the program. If a user enters non-numeric text for marks or an invalid choice, the application displays a friendly warning and prompts again using `while` loops.
3. **Data Integrity**: Roll numbers are verified for uniqueness before adding new students, preventing duplicate entries. When updating, users can press Enter to keep existing values.
4. **Immediate Feedback**: Whenever marks are entered or modified, the result card is immediately computed and displayed so the user can verify their input on the spot.

---

## Learning Outcomes

Through building this project, I strengthened my practical understanding of:
- Structuring a CLI application with clean menu loops and modular functions.
- Storing, updating, and querying complex in-memory datasets using nested dictionaries inside lists.
- Writing defensive code with `try...except` and range bounds checking.
- Generating formatted reports and calculating aggregate statistical metrics like class averages and distributions.
