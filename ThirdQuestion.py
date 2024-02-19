Q3. Which Python statements are used to catch and handle exceptions? Explain with an example.
In Python, the try, except, else, and finally statements are used to catch and handle exceptions. Here's how they work:

try: The try block contains the code that might raise an exception.
except: The except block is executed if an exception occurs in the corresponding try block. It specifies the type of exception to catch.

else (optional): The else block is executed if no exceptions are raised in the try block. It is optional and provides a block of code to run when no exceptions occur.

finally (optional): The finally block is always executed, regardless of whether an exception occurs or not. It is optional and provides a block of code that will be executed no matter what.
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division successful.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("No exceptions occurred.")
    finally:
        print("This block always runs, regardless of exceptions.")

divide_numbers(10, 2)

divide_numbers(10, 0)
