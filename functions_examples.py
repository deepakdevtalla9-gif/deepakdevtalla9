# Functions, parameters, return values, lambda, and list comprehensions

# 1. Function with no parameters
def greet():
    print("Hello, Python learner!")


# 2. Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")


# 3. Function that returns a value
def add_numbers(a, b):
    return a + b


# 4. Default parameter
def introduce(name, course="Python"):
    return f"My name is {name} and I am learning {course}."


# 5. Keyword arguments
def student_details(name, age):
    return f"Name: {name}, Age: {age}"


# 6. Lambda function
square = lambda number: number * number

# 7. List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]


if __name__ == "__main__":
    greet()
    greet_user("Deepak")
    print("Sum:", add_numbers(10, 20))
    print(introduce("Deepak"))
    print(student_details(age=21, name="Deepak"))
    print("Square:", square(6))
    print("Squares:", squares)
    print("Even numbers:", even_numbers)
