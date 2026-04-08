def count_divisors(x):
    if x == 1:
        return 1
    
    count = 0
    i = 1
    # Идём только до квадратного корня
    while i * i <= x:
        if x % i == 0:
            # Если делители равны (квадратный корень)
            if i == x // i:
                count += 1
            else:
                # Иначе считаем оба делителя: i и x//i
                count += 2
        i += 1
    return count

# Считываем число
x = int(input())
print(count_divisors(x))