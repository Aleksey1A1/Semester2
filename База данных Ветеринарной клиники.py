import collections

# Исходная база данных с питомцами
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}


def get_pet(ID):
    """
    Функция для получения информации о питомце по его ID
    Возвращает словарь с информацией о питомце, если ID существует
    Иначе возвращает False
    """
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    """
    Функция для определения правильного суффикса для возраста
    'год', 'года', 'лет'
    """
    if 10 <= age % 100 <= 20:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def pets_list():
    """
    Функция для отображения всего списка питомцев
    """
    if not pets:
        print("База данных пуста.")
        return
    
    print("\n=== СПИСОК ВСЕХ ПИТОМЦЕВ ===")
    for pet_id, pet_info in pets.items():
        # Получаем имя питомца (первый ключ во вложенном словаре)
        pet_name = list(pet_info.keys())[0]
        pet_data = pet_info[pet_name]
        
        print(f"ID: {pet_id} | {pet_name} - {pet_data['Вид питомца']}, "
              f"{pet_data['Возраст питомца']} {get_suffix(pet_data['Возраст питомца'])}, "
              f"владелец: {pet_data['Имя владельца']}")
    print("=" * 40)


def create():
    """
    Функция для создания новой записи о питомце
    """
    print("\n--- ДОБАВЛЕНИЕ НОВОГО ПИТОМЦА ---")
    
    # Получаем последний ID
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1
    
    # Запрашиваем информацию о питомце
    name = input("Введите кличку питомца: ").strip()
    animal_type = input("Введите вид питомца: ").strip()
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ").strip()
    
    # Создаем запись
    pets[new_id] = {
        name: {
            "Вид питомца": animal_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    
    print(f"✅ Питомец '{name}' успешно добавлен с ID: {new_id}")


def read():
    """
    Функция для отображения информации о конкретном питомце
    """
    print("\n--- ПОИСК ПИТОМЦА ---")
    pet_id = int(input("Введите ID питомца: "))
    
    pet_info = get_pet(pet_id)
    
    if pet_info is False:
        print(f"❌ Питомец с ID {pet_id} не найден!")
        return
    
    # Получаем имя питомца
    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    
    # Выводим информацию в требуемом формате
    print(f"\nЭто {pet_data['Вид питомца']} по кличке \"{pet_name}\". "
          f"Возраст питомца: {pet_data['Возраст питомца']} {get_suffix(pet_data['Возраст питомца'])}. "
          f"Имя владельца: {pet_data['Имя владельца']}")


def update():
    """
    Функция для обновления информации о питомце
    """
    print("\n--- ОБНОВЛЕНИЕ ИНФОРМАЦИИ О ПИТОМЦЕ ---")
    pet_id = int(input("Введите ID питомца для обновления: "))
    
    pet_info = get_pet(pet_id)
    
    if pet_info is False:
        print(f"❌ Питомец с ID {pet_id} не найден!")
        return
    
    # Получаем имя питомца
    pet_name = list(pet_info.keys())[0]
    pet_data = pet_info[pet_name]
    
    print(f"\nТекущая информация о питомце: {pet_name}")
    print(f"Вид: {pet_data['Вид питомца']}")
    print(f"Возраст: {pet_data['Возраст питомца']}")
    print(f"Владелец: {pet_data['Имя владельца']}")
    
    print("\nВведите новые данные (оставьте поле пустым, чтобы не менять):")
    
    new_name = input(f"Новая кличка (было: {pet_name}): ").strip()
    new_type = input(f"Новый вид (было: {pet_data['Вид питомца']}): ").strip()
    new_age = input(f"Новый возраст (было: {pet_data['Возраст питомца']}): ").strip()
    new_owner = input(f"Новое имя владельца (было: {pet_data['Имя владельца']}): ").strip()
    
    # Обновляем данные
    if new_name:
        # Если меняется имя, нужно создать новый ключ
        old_name = pet_name
        new_pet_data = pet_data.copy()
        if new_type:
            new_pet_data["Вид питомца"] = new_type
        if new_age:
            new_pet_data["Возраст питомца"] = int(new_age)
        if new_owner:
            new_pet_data["Имя владельца"] = new_owner
        
        # Удаляем старую запись и создаем новую с новым именем
        del pets[pet_id][old_name]
        pets[pet_id][new_name] = new_pet_data
    else:
        # Обновляем существующие поля
        if new_type:
            pet_data["Вид питомца"] = new_type
        if new_age:
            pet_data["Возраст питомца"] = int(new_age)
        if new_owner:
            pet_data["Имя владельца"] = new_owner
    
    print(f"✅ Информация о питомце успешно обновлена!")


def delete():
    """
    Функция для удаления записи о питомце
    """
    print("\n--- УДАЛЕНИЕ ПИТОМЦА ---")
    pet_id = int(input("Введите ID питомца для удаления: "))
    
    pet_info = get_pet(pet_id)
    
    if pet_info is False:
        print(f"❌ Питомец с ID {pet_id} не найден!")
        return
    
    # Получаем имя питомца для подтверждения
    pet_name = list(pet_info.keys())[0]
    
    confirm = input(f"Вы уверены, что хотите удалить питомца '{pet_name}'? (да/нет): ").lower()
    
    if confirm == 'да' or confirm == 'yes':
        del pets[pet_id]
        print(f"✅ Питомец '{pet_name}' успешно удален!")
    else:
        print("❌ Удаление отменено.")


# Основная программа
def main():
    """
    Главная функция программы с циклом while
    """
    print("=" * 50)
    print("🐾 ВЕТЕРИНАРНАЯ КЛИНИКА - БАЗА ДАННЫХ")
    print("=" * 50)
    print("Доступные команды:")
    print("  create - добавить нового питомца")
    print("  read   - показать информацию о питомце")
    print("  update - обновить информацию о питомце")
    print("  delete - удалить питомца")
    print("  list   - показать всех питомцев")
    print("  stop   - завершить работу программы")
    print("=" * 50)
    
    while True:
        command = input("\nВведите команду: ").strip().lower()
        
        if command == 'stop':
            print("👋 Программа завершена. До свидания!")
            break
        elif command == 'create':
            create()
        elif command == 'read':
            read()
        elif command == 'update':
            update()
        elif command == 'delete':
            delete()
        elif command == 'list':
            pets_list()
        else:
            print("❌ Неизвестная команда. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()