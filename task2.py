# task2.py

# запрашиваем числа у пользователя
num1 = input('первое число: ')
num2 = input('второе число: ')
# проверяем, что строки - это числа
if num1.isnumeric() and num2.isnumeric():
	num1 = int(num1)
	num2 = int(num2)
	# проверка деления на ноль
	if num2 != 0:
		print(num1/num2)
	# выводим сообщения об ошибках
	else:
		print('деление на ноль!')
else:
	print('не число!')
