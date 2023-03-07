num = int(input())
if 999 < num < 10000:
    a = num // 1000
    b = (num // 100) % 10
    c = (num // 10) % 10
    d = num % 10
    if a + b == c + d:
        print("Поздравляю, они равны")
    if (a + b + c + d) % 3 == 0:
        print("Кратно")
    if (a * b * c * d) % 4 == 0:
        print("Кратно * Кратно")
    if num % (a * b * c * d) == 0:
        print("Ультра кратно")