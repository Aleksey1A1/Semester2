# Получаем пятизначное число от пользователя
number = int(input("Введите пятизначное число от пользователя:"))

# Извлекаем цыфры числа
# Десятки тысяч - первая цыфра
ten_thousands = number // 10000

# Тысячи - вторая цифра
thousands = (number // 1000) % 10

# Сотни - третья цифра
hundreds = (number // 100) % 10

# Десятки - четвертая цифра
tens = (number // 10) % 10

# Единицы - пятая цифра
units = number % 10

# Выведим полученные цифры для наглядности
print(f"Цифры числа {number}:")
print(f"Десятки тысяч:{ten_thousands}")
print(f"Тысячи: {thousands}")
print(f"Сотни: {hundreds}")
print(f"Десятки: {tens}")
print(f"Единици: {units}")

# Выполняем вычисление по алгоритму
# 1. Возводим в степень едениц
step1 = tens ** units

# 2. Умножаем на количество сотен
step2 = step1 * hundreds

# 3. Находим разность десятков тысяч и тысяч
difference = ten_thousands - thousands

# 4. Делим результаты на разность 
result = step2 / difference

# Выводим результат
print(f"\nРезультат вычислений: {result}")
print(f"Проверка: {tens}^{units} * {hundreds} / ({ten_thousands} - {thousands}) = {result}")