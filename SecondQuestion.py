Q2. What happens when an exception is not handled? Explain with an example.
When an exception is not handled in a program, it leads to the termination of the program and the display of an error traceback. The error traceback provides information about the type of exception, the line number where the exception occurred, and the sequence of function calls that led to the exception.
def divide_numbers(a, b):
    result = a / b
    return result
result = divide_numbers(10, 0)
print("Result:", result)
