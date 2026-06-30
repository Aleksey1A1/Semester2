n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

# Переворачиваем массив
arr.reverse()

# Выводим результат
for num in arr:
    print(num)