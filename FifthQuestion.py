Q5. What are Custom Exceptions in python? Why do we need Custom Exceptions? Explain with an example.
Custom exceptions in Python are user-defined exceptions that extend the functionality of the built-in exceptions provided by the language. Programmers can create their own exception classes by deriving them from the base Exception class or one of its subclasses. These custom exceptions allow developers to handle specific error conditions in a more granular and meaningful way.

Why do we need Custom Exceptions?
Granular Error Handling: Custom exceptions provide a way to handle specific error conditions that may be unique to a particular application or module. This allows for more precise error handling and facilitates debugging by providing specific information about the nature of the error.

Code Readability: By using custom exceptions, code readability is improved because the exception names can convey the meaning of the error more clearly. This makes it easier for other developers (or even the original developer) to understand the purpose and nature of the exceptions being raised.

Modularity: Custom exceptions promote modularity in code. Each module or subsystem can define its own exceptions tailored to its specific requirements, making it easier to maintain and extend the codebase.
class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value ({self.value}) is not allowed.")

def process_positive_number(number):
    try:
        if number < 0:
            raise NegativeValueError(number)
        else:
            print("Processing positive number:", number)
    except NegativeValueError as e:
        print(f"Error: {e}")

process_positive_number(10)      
process_positive_number(-5)      
