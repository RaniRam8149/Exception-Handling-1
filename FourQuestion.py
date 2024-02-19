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
