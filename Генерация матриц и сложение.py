import random

def generate_matrix(rows, cols, min_val=-100, max_val=100):
    """Генерирует матрицу заданного размера со случайными целыми числами."""
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def print_matrix(matrix, name="Матрица"):
    """Красиво выводит матрицу."""
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()

def add_matrices(matrix1, matrix2):
    """Складывает две матрицы одинаковой размерности."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Проверка размерностей
    if rows != len(matrix2) or cols != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинаковой размерности!")
    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# ============== ЧАСТЬ 1: Сложение готовых матриц (проверка) ==============
print("=" * 50)
print("ЧАСТЬ 1: Сложение готовых матриц")
print("=" * 50)

matrix_1 = [
    [0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
    [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
    [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
    [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
    [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
    [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
    [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
    [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
    [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
    [43, 111, 38, 149, 5, 112, 79, 53, 15, 92]
]

matrix_2 = [
    [0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
    [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
    [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
    [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
    [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
    [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
    [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
    [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
    [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
    [32, -67, -75, -92, 15, -163, 18, 31, -162, -16]
]

matrix_3_expected = [
    [0, 2, 5, 5, 9, 6, 0, 18, -15, 12],
    [0, 16, -11, -25, -8, -7, -24, 4, -3, -27],
    [11, 0, -5, 37, 18, 45, -2, 21, 8, 14],
    [-9, -60, 45, 38, 27, 34, 36, 5, -56, 9],
    [-40, 26, 66, 3, 15, 66, -6, -14, 5, 69],
    [46, 48, 44, 41, 86, -99, -14, -7, 29, 94],
    [75, 81, 5, 130, -11, -44, -1, -70, -104, -101],
    [-113, -19, -46, -132, -11, 110, -43, 10, -123, -8],
    [-47, 45, 87, 5, -105, -161, -70, -95, -4, 0],
    [75, 44, -37, 57, 20, -51, 97, 84, -147, 76]
]

matrix_3_calculated = add_matrices(matrix_1, matrix_2)

print_matrix(matrix_1, "matrix_1")
print_matrix(matrix_2, "matrix_2")
print_matrix(matrix_3_calculated, "matrix_3 (результат сложения)")

# Проверка, совпадает ли с ожидаемым
if matrix_3_calculated == matrix_3_expected:
    print("✓ Сложение готовых матриц выполнено верно!")
else:
    print("✗ Ошибка: результат не совпадает с ожидаемым!")
print()

# ============== ЧАСТЬ 2: Генерация случайных матриц и их сложение ==============
print("=" * 50)
print("ЧАСТЬ 2: Генерация случайных матриц 10x10")
print("=" * 50)

# Генерируем две матрицы 10x10 со случайными значениями
matrix_a = generate_matrix(10, 10, -200, 200)
matrix_b = generate_matrix(10, 10, -200, 200)

# Складываем их
matrix_c = add_matrices(matrix_a, matrix_b)

print_matrix(matrix_a, "Случайная матрица A (10x10)")
print_matrix(matrix_b, "Случайная матрица B (10x10)")
print_matrix(matrix_c, "Матрица C = A + B (10x10)")

# ============== ЧАСТЬ 3: Генерация матриц произвольной размерности ==============
print("=" * 50)
print("ЧАСТЬ 3: Генерация матриц произвольной размерности")
print("=" * 50)

# Пример с размерностью 4x3
rows, cols = 4, 3
matrix_d = generate_matrix(rows, cols, -50, 50)
matrix_e = generate_matrix(rows, cols, -50, 50)
matrix_f = add_matrices(matrix_d, matrix_e)

print(f"Матрица D ({rows}x{cols}):")
for row in matrix_d:
    print(row)
print()

print(f"Матрица E ({rows}x{cols}):")
for row in matrix_e:
    print(row)
print()

print(f"Матрица F = D + E ({rows}x{cols}):")
for row in matrix_f:
    print(row)
print()

# ============== ЧАСТЬ 4: Демонстрация с размерностью 5x7 ==============
print("=" * 50)
print("ЧАСТЬ 4: Ещё один пример (5x7)")
print("=" * 50)

matrix_g = generate_matrix(5, 7, -100, 100)
matrix_h = generate_matrix(5, 7, -100, 100)
matrix_i = add_matrices(matrix_g, matrix_h)

print("Матрица G (5x7):")
for row in matrix_g:
    print(row)
print()

print("Матрица H (5x7):")
for row in matrix_h:
    print(row)
print()

print("Матрица I = G + H (5x7):")
for row in matrix_i:
    print(row)
print()

print("=" * 50)
print("Задание выполнено! Алгоритм умеет:")
print("1. Генерировать матрицы любой размерности со случайными числами")
print("2. Складывать матрицы одинаковой размерности")
print("=" * 50)