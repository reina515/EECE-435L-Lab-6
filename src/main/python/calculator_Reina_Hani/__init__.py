import math


# adds two numbers
def add(x, y):
    return x + y


# subtracts y from x
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


# divides x by y, can't divide by zero
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


# returns the remainder of x divided by y
def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot take modulus by zero.")
    return x % y


# raises x to the power of y
def power(x, y):
    return x ** y


# returns the square root of x, only works for non negative numbers
def square_root(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)
