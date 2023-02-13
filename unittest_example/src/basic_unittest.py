def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by 0")
    return x / y

def multiply(x,y):
    return x * y