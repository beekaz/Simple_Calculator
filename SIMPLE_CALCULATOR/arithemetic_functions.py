<<<<<<< HEAD
from main_function import  Tk, Label
def add(a, b):
=======
from main_function import *
def add(a: float, b: float) -> float:
>>>>>>> a37f744 (Annotate functions in arithemetic_functions module)
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b != 0:
        result = num1 / num2
        label_result = Tk.Label(frame, text="Result: {result}")
        label_result.pack()
#        label_result.config(text=f"Result: {result}")
        return a / b
    
    else:
        print("error")
        return 0
    
# Get input from the user
num1 = float(input("Enter the first number: "))
operation = input("Enter the operation:")
num2 = float(input("Enter the second number: "))

# Perform the selected operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Error: Invalid operation.")
    result = 0

# Print the result
print("Result:", result)
