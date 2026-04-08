# Считываем A и B
A, B = map(int, input().split())

# Собираем четные числа в список
even_numbers = []

for i in range(A, B + 1):
    if i % 2 == 0:
        even_numbers.append(i)

# Выводим через пробел
print(*even_numbers)