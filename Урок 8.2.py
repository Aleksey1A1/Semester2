n = int(input())
arr = list(map(int, input().split()))

# Метод для преобразования массива
def transform_array(arr):
    if not arr:
        return
    # Сохраняем последний элемент
    last = arr[-1]
    # Сдвигаем все элементы вправо на 1 позицию
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    # Ставим последний элемент на первое место
    arr[0] = last

transform_array(arr)
print(*arr)