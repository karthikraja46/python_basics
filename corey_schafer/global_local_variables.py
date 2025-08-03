# Local variables are created within a function and exist only during its execution. They're not accessible from outside the function.
#local variable
def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()

# Global variables are defined outside all functions. They can be accessed and used in any part of the program, including inside functions
#global variable
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)