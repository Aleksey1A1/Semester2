class Turtle:
    """
    Класс, представляющий черепашку, которая перемещается по координатной сетке.
    """
    
    def __init__(self, x=0, y=0, s=1):
        """
        Инициализация черепашки с начальными координатами и шагом.
        
        Args:
            x (int): Начальная координата X
            y (int): Начальная координата Y
            s (int): Количество клеток за один ход (должно быть > 0)
        """
        if s <= 0:
            raise ValueError("Шаг s должен быть положительным числом")
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        """Увеличивает y на s (движение вверх)."""
        self.y += self.s
        print(f"Движение вверх. Новая позиция: ({self.x}, {self.y})")
    
    def go_down(self):
        """Уменьшает y на s (движение вниз)."""
        self.y -= self.s
        print(f"Движение вниз. Новая позиция: ({self.x}, {self.y})")
    
    def go_left(self):
        """Уменьшает x на s (движение влево)."""
        self.x -= self.s
        print(f"Движение влево. Новая позиция: ({self.x}, {self.y})")
    
    def go_right(self):
        """Увеличивает x на s (движение вправо)."""
        self.x += self.s
        print(f"Движение вправо. Новая позиция: ({self.x}, {self.y})")
    
    def evolve(self):
        """Увеличивает s на 1."""
        self.s += 1
        print(f"Эволюция! Шаг увеличен до {self.s}")
    
    def degrade(self):
        """
        Уменьшает s на 1.
        Выбрасывает ошибку, если s станет ≤ 0.
        """
        if self.s - 1 <= 0:
            raise ValueError(f"Невозможно уменьшить шаг! Текущий шаг: {self.s}, после уменьшения станет {self.s - 1} (≤ 0)")
        self.s -= 1
        print(f"Деградация! Шаг уменьшен до {self.s}")
    
    def count_moves(self, x2, y2):
        """
        Возвращает минимальное количество действий, за которое черепашка 
        сможет добраться до позиции (x2, y2) от текущей позиции.
        
        Действием считается:
        - Одно перемещение (вверх/вниз/влево/вправо) на s клеток
        - evolve() - увеличивает s на 1
        - degrade() - уменьшает s на 1
        
        Args:
            x2 (int): Целевая координата X
            y2 (int): Целевая координата Y
        
        Returns:
            int: Минимальное количество действий
        """
        # Вычисляем разницу по осям
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        
        # Если черепашка уже на месте
        if dx == 0 and dy == 0:
            return 0
        
        # (Минимальное количество шагов при текущем s)
        # Но нужно учесть, что s может меняться через evolve/degrade
        
        # Простой подход: считаем, что нам нужно покрыть расстояние dx + dy
        # Каждым перемещением мы проходим s клеток
        # Если s не хватает, нужно увеличивать s через evolve
        # Но evolve тоже считается за действие
        
        total_distance = dx + dy
        
        # Если можно дойти текущим s
        if total_distance % self.s == 0:
            moves = total_distance // self.s
        else:
            # Нужно либо увеличить s, либо сделать больше шагов
            # Минимальное количество действий - это min(эволюционировать до нужного s, или сделать доп шаги)
            
            # Вариант 1: Дойти с текущим s, сделав ceil(total_distance / s) шагов
            import math
            moves_with_current_s = math.ceil(total_distance / self.s)
            
            # Вариант 2: Увеличить s до такого значения, чтобы total_distance делилось нацело
            # Но увеличение s тоже требует действий (evolve)
            # Попробуем увеличить s на 1 и проверить
            best_moves = moves_with_current_s
            
            # Проверяем варианты с изменением s
            # Ограничимся разумным перебором
            for new_s in range(self.s + 1, self.s + 20):  # Проверяем увеличение s
                if total_distance % new_s == 0:
                    # Действия: (new_s - self.s) раз evolve + total_distance // new_s шагов
                    total_actions = (new_s - self.s) + (total_distance // new_s)
                    best_moves = min(best_moves, total_actions)
                else:
                    # Можно сделать ceil
                    total_actions = (new_s - self.s) + math.ceil(total_distance / new_s)
                    best_moves = min(best_moves, total_actions)
            
            # Проверяем вариант с уменьшением s (если это возможно)
            for new_s in range(1, self.s):  # Проверяем уменьшение s
                if total_distance % new_s == 0:
                    total_actions = (self.s - new_s) + (total_distance // new_s)
                    best_moves = min(best_moves, total_actions)
                else:
                    total_actions = (self.s - new_s) + math.ceil(total_distance / new_s)
                    best_moves = min(best_moves, total_actions)
            
            moves = best_moves
        
        print(f"Минимальное количество действий от ({self.x}, {self.y}) до ({x2}, {y2}): {moves}")
        return moves


# Пример использования:
if __name__ == "__main__":
    # Создаём черепашку в точке (0, 0) с шагом 1
    turtle = Turtle(0, 0, 1)
    
    # Перемещения
    turtle.go_up()      # (0, 1)
    turtle.go_right()   # (1, 1)
    turtle.go_up()      # (1, 2)
    
    # Эволюция
    turtle.evolve()     # s = 2
    
    # Перемещения с новым шагом
    turtle.go_up()      # (1, 4)
    turtle.go_right()   # (3, 4)
    
    # Подсчёт минимальных действий до точки (10, 10)
    turtle.count_moves(10, 10)
    
    # Деградация
    turtle.degrade()    # s = 1
    
    # Попытка деградировать до 0 (выбросит ошибку)
    try:
        turtle.degrade()  # s станет 0 -> ошибка
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Создаём новую черепашку для демонстрации count_moves
    print("\n--- Демонстрация count_moves ---")
    t2 = Turtle(2, 2, 2)
    print(f"Старт: ({t2.x}, {t2.y}), шаг: {t2.s}")
    t2.count_moves(2, 2)  # Нужно дойти до (2, 2)