# Python Module 02: Functions, Files & Exception Handling

This repository contains beginner-friendly Python examples for Module 02 (Day 6–Day 10).

## Topics covered
- Functions, parameters, return values
- Lambda functions and list comprehensions
- File handling with CSV and JSON
- Exception handling with `try`, `except`, and `finally`
- Basic debugging practices
- Python virtual environments
- Student Record Management System with CRUD operations

## Project: Student Record Management System
The program lets you:
1. Add a student
2. View all students
3. Search for a student by ID
4. Update a student record
5. Delete a student record
6. Choose CSV or JSON as the storage format

## Requirements
- Python 3.9 or newer
- No third-party packages required

## Run the project
Open a terminal in this repository folder and run:

```bash
python student_record_system/main.py
```

On some Windows systems, use `py` instead of `python`.

## Example data
The application creates its data file when you add a record. Sample CSV and JSON files are included in `student_record_system/sample_data/`.

## Virtual environment (optional)
```bash
python -m venv .venv
```
Activate it:
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Deactivate it with:
```bash
deactivate
```

## Repository structure
```text
Python_Module_02_Functions_Files_Exception_Handling/
├── README.md
├── examples/
│   ├── functions_examples.py
│   ├── file_handling_examples.py
│   └── exception_examples.py
├── notes/
│   └── learning_notes.md
└── student_record_system/
    ├── main.py
    └── sample_data/
        ├── students.csv
        └── students.json
```

## Learning note
This project is for practice. Test each menu option and read the code to understand how each operation works.
