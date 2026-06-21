# Читаем первый список
list1 = list(map(int, input().split()))
# Читаем второй список
list2 = list(map(int, input().split()))

# Преобразуем в множества для эффективного поиска
set1 = set(list1)
set2 = set(list2)

# Находим пересечение и считаем его длину
common_count = len(set1 & set2)

print(common_count)