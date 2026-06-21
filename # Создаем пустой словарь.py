# Создаем пустой словарь
pets = {}

# Запрашиваем информацию у пользователя
name = input("Введите имя питомца: ")
animal_type = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

# Заполняем словарь
pets[name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": age,
    "Имя владельца": owner
}

# Функция для правильного склонения слова "год"
def get_age_string(age):
    if 11 <= age % 100 <= 19:
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif 2 <= age % 10 <= 4:
        return f"{age} года"
    else:
        return f"{age} лет"

# Выводим информацию о питомце
for pet_name, pet_info in pets.items():
    # Получаем значения из словаря
    animal_type = pet_info["Вид питомца"]
    age = pet_info["Возраст питомца"]
    owner = pet_info["Имя владельца"]
    
    # Формируем строку с правильным склонением
    age_str = get_age_string(age)
    
    # Выводим результат
    print(f'Это {animal_type} по кличке "{pet_name}". Возраст питомца: {age_str}. Имя владельца: {owner}')