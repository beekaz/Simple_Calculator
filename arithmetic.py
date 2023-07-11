"""
Arithmetic functions.
This module is irrelevant to the simple calculator.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    return a / b


if __name__ == "__main__":
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation: ").strip()
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    result: float | str = 0.0

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation in {"*", "x", "X"}:
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Operation not supported"
    print(f"{num1} {operation} {num2} = {result}")
