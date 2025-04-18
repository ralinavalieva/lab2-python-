# task1.py

# создаем файл data.txt с 10 числами
with open('data.txt', 'w') as f:
    for i in range(10):
        f.write(f"{i + 1}\n")  # записываем числа от 1 до 10

# читаем числа из файла
with open('data.txt', 'r') as f:
    nums = [int(line.strip()) for line in f]

# вычисляем сум, ср, макс и мин
total_sum = sum(nums)
average = total_sum / len(nums)
maximum = max(nums)
minimum = min(nums)

# сохраняем результаты в result.txt
with open('result.txt', 'w') as f:
    f.write(f"сумма: {total_sum}\n")
    f.write(f"среднее: {average}\n")
    f.write(f"максимум: {maximum}\n")
    f.write(f"минимум: {minimum}\n")

# выводим результаты в консоль
print(f"сумма: {total_sum}, среднее: {average}, максимум: {maximum}, минимум: {minimum}")