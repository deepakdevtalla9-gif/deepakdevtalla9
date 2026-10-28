# Module 02 Learning Notes: Functions, Files & Exception Handling

## 1. Functions
A function is a reusable block of code that performs a task. Define it using `def`.

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Deepak"))
```

- **Parameter:** the variable written in the function definition, such as `name`.
- **Argument:** the value passed when calling the function, such as `"Deepak"`.
- **Return value:** the result sent back using `return`.
- **Default parameter:** a parameter with a default value, for example `def greet(name="Friend")`.
- **Lambda:** a short anonymous function, for example `square = lambda x: x * x`.

## 2. List comprehensions
List comprehensions create a list in a compact way.

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

## 3. File handling
Use `with open(...)` to open files safely. The file closes automatically after the block.

- `r`: read
- `w`: write, replacing existing content
- `a`: append
- `newline=""`: recommended when using Python's CSV module
- Use `encoding="utf-8"` for text files.

### CSV
CSV stores tabular data as rows and columns. Python's `csv.DictReader` reads each row as a dictionary, and `csv.DictWriter` writes dictionaries.

### JSON
JSON stores structured data such as lists and dictionaries. Use `json.dump()` to write and `json.load()` to read.

## 4. Exception handling
Exceptions are errors that occur while a program runs. Handling them lets the program respond clearly instead of crashing unexpectedly.

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a whole number.")
finally:
    print("Input step finished.")
```

- `try`: code that may raise an exception.
- `except`: handles a matching exception.
- `finally`: runs whether an exception occurred or not.
- Catch specific exceptions where possible, rather than using a bare `except`.

## 5. Debugging tips
1. Read the error message and traceback.
2. Find the line number mentioned.
3. Check spelling, indentation, data types, and variable names.
4. Print values to understand the program's state.
5. Reproduce the issue with a small input.
6. Test normal input, invalid input, and edge cases.

## 6. Virtual environments
A virtual environment keeps a project's installed packages separate from other Python projects.

Create:
```bash
python -m venv .venv
```

Activate on Windows PowerShell:
```powershell
.venv\\Scripts\\Activate.ps1
```

Activate on macOS/Linux:
```bash
source .venv/bin/activate
```

Leave the environment:
```bash
deactivate
```

This project uses only Python's standard library, so no extra packages are required.

## 7. CRUD operations
CRUD stands for:
- **Create:** add a record
- **Read:** view or search records
- **Update:** edit an existing record
- **Delete:** remove a record

The Student Record Management System implements all four operations and saves records in CSV or JSON format.
