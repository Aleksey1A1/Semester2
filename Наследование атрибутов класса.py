class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def display_info(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"


class Autobus(Transport):
    pass  # Наследует все от родительского класса


# Создаем объект Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию
print(bus.display_info())