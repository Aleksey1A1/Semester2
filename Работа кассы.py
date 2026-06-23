class CashBox:
    """
    Класс, представляющий кассу для хранения денег.
    """
    
    def __init__(self, initial_amount=0):
        """
        Инициализация кассы с начальной суммой (по умолчанию 0).
        """
        if initial_amount < 0:
            raise ValueError("Начальная сумма не может быть отрицательной")
        self.money = initial_amount
    
    def top_up(self, X):
        """
        Пополнить кассу на X рублей.
        X должно быть положительным числом.
        """
        if X < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной")
        self.money += X
        print(f"Касса пополнена на {X} руб. Текущий баланс: {self.money} руб.")
    
    def count_1000(self):
        """
        Выводит и возвращает количество целых тысяч в кассе.
        """
        thousands = self.money // 1000
        print(f"В кассе {thousands} целых тысяч рублей")
        return thousands
    
    def take_away(self, X):
        """
        Забрать X рублей из кассы.
        Выбрасывает исключение, если денег недостаточно.
        """
        if X < 0:
            raise ValueError("Сумма для снятия не может быть отрицательной")
        
        if X > self.money:
            raise Exception(f"Недостаточно денег! Требуется: {X} руб., Доступно: {self.money} руб.")
        
        self.money -= X
        print(f"Из кассы забрали {X} руб. Остаток: {self.money} руб.")
        return X


# Пример использования:
if __name__ == "__main__":
    # Создаём кассу с 5000 рублей
    cash_box = CashBox(5000)
    
    # Пополняем на 3000
    cash_box.top_up(3000)  # Баланс: 8000
    
    # Сколько тысяч?
    cash_box.count_1000()  # 8 тысяч
    
    # Забираем 2500
    cash_box.take_away(2500)  # Баланс: 5500
    
    # Пробуем забрать больше, чем есть
    try:
        cash_box.take_away(6000)  # Выбрасывает исключение!
    except Exception as e:
        print(f"Ошибка: {e}")