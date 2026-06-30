m = int(input())  # максимальная масса лодки
n = int(input())  # количество рыбаков
weights = [int(input()) for _ in range(n)]

# Сортируем веса по возрастанию
weights.sort()

boats = 0
left = 0
right = n - 1

# Используем два указателя
while left <= right:
    if left == right:
        # Остался один рыбак
        boats += 1
        break
    
    # Если самый тяжелый и самый легкий помещаются вместе
    if weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        # Самый тяжелый едет один
        right -= 1
    
    boats += 1

print(boats)