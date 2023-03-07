num = int(input())
if 100 <= num <= 999:
    a = num // 100
    b = (num % 100) // 10
    c = num % 10
    if 9 < (a + b + c) < 100:
        print(a + b+ c)
    if 99 < (a * b * c) < 1000:
        print(a * b * c)
    if num > (a * b * c):
        print("Польша")
    if (a + b + c) % 5 == 0:
        print("Кратно")
    if num % (a + b + c) == 0:
        print("Кратно: возвращение")