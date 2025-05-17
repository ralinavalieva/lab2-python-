# task5.py

# создаем список чисел от 1 до 20
nums = list(range(1, 21))

# используем лямбда-функции для фильтрации и обработки списка
even_nums = list(filter(lambda x: x % 2 == 0, nums))
increased_nums = list(map(lambda x: x + 10, even_nums))
sorted_nums = sorted(increased_nums, reverse=True)#сорт. получ. числа по убыванию 

# выводим результаты
print("четные числа:", even_nums)
print("четные числа увеличенные на 10:", increased_nums)
print("отсортированные по убыванию:", sorted_nums)
