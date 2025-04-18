# task2.py

try:
    # запрашиваем два числа у пользователя
    num1 = float(input("введите первое число: "))
    num2 = float(input("введите второе число: "))

    # выполняем деление
    res = num1 / num2
except ZeroDivisionError:
    print("ошибка: деление на ноль!")
except ValueError:
    print("ошибка: вводите только числовые значения!")
else:
    print(f"результат деления {num1} на {num2}: {result}")