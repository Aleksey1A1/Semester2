X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Деньги Майкла: "))
B = int(input("Деньги Ивана: "))

# Проверяем возможности
can_mike = A >= X
can_ivan = B >= X
can_together = (A + B) >= X

if can_mike and can_ivan:
    print(2)
elif can_mike and not can_ivan:
    print("Mike")
elif not can_mike and can_ivan:
    print("Ivan")
elif not can_mike and not can_ivan and can_together:
    print(1)
else:
    print(0)