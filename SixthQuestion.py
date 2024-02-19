Q6. Create a custom exception class. Use this class to handle an exception.
 In this example, we'll create a custom exception called InvalidInputError to handle situations where an invalid input is encountered.
class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        super().__init__(f"Invalid input: {self.input_value}")

def process_input(data):
    try:
        if not isinstance(data, int):
            raise InvalidInputError(data)
        else:
            print("Processing input:", data)
    except InvalidInputError as e:
        print(f"Error: {e}")

process_input(42)       
process_input("abc")   
