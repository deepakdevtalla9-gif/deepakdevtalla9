# Exception handling examples

# 1. Handling invalid numeric input
try:
    number = int(input("Enter a whole number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a whole number.")

# 2. Handling division by zero
try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    print("Result:", first / second)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
finally:
    print("Division example finished.")

# Debugging tips:
# - Read the last line of the traceback first.
# - Check the line number mentioned in the error.
# - Print variable values to understand program flow.
# - Reproduce the error with a small input.
