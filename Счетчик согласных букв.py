word = input("Введите слово из маленьких латинских букв: ")

# Гласные буквы
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0

# Счетчики для каждой гласной
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Подсчет
for letter in word:
    if letter in vowels:
        vowel_count += 1
        if letter == 'a':
            count_a += 1
        elif letter == 'e':
            count_e += 1
        elif letter == 'i':
            count_i += 1
        elif letter == 'o':
            count_o += 1
        elif letter == 'u':
            count_u += 1
    else:
        consonant_count += 1

# Вывод результатов
print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")

# Вывод количества каждой гласной или False, если буквы нет
print(f"a: {count_a if count_a > 0 else False}")
print(f"e: {count_e if count_e > 0 else False}")
print(f"i: {count_i if count_i > 0 else False}")
print(f"o: {count_o if count_o > 0 else False}")
print(f"u: {count_u if count_u > 0 else False}")