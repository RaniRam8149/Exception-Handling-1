Q4. Explain with an example:

a. try and else
In this example, the try block contains code that might raise an exception, and the else block contains code that will only run if no exceptions occur.
try:
    f=open("test.txt",'w')
    f.write("write into my file")
    f.close()
except Exception as e:
    print("this is my except block")
else:
    f.close()
    print("this will be exxecuted once your try will execute without error")
    
b. Finally
In this example, the finally block contains code that will always run, regardless of whether an exception occurs or not.
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division successful. Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("This block always runs, regardless of exceptions.")

divide_numbers(10, 2)

divide_numbers(10, 0)

c. raise
In this example, the raise statement is used to deliberately raise a custom exception.
class validataege(Exception):
    def __init__(self,msg):
        self.msg=msg

def validaetage(age):
    if age<0:
        raise validateage("entered age is negative")
    elif age>200:
        raise validateage("entered age is very high")
    else:
        print("age is valid")

try:
    age=int(input("enter your age"))
    validaetage(age)
except validaetage as e:
    print(e)
