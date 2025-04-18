# task3.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("деление на ноль невозможно.")
    return a / b
    
    # task3.py

from task3 import add, subtract, multiply, divide

# пример использования функций модуля
a = 10
b = 5

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")

try:
    print(f"{a} / {b} = {divide(a, b)}")
except ValueError as e:
    print(e)