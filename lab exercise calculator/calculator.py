
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 20. A developer accidentally changes this line:
def multiply(a, b):    
       return a * b + 1

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    return a % b
