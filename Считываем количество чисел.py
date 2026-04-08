N = int(input())  # Считываем количество чисел
count_zero = 0    # Счётчик нулей

# Считываем N чисел и проверяем каждое
for _ in range(N):
    number = int(input())
    if number == 0:
        count_zero += 1

# Выводим результат
print(count_zero)