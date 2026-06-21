# Создаем пустой словарь
my_dict = {}

# Цикл от 10 до -5 включительно (с шагом -1)
for num in range(10, -6, -1):
    my_dict[num] = num ** num

# Выводим результат
print(my_dict)