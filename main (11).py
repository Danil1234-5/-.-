a = int(input("Введите двух значное число = "))
if 9 < a < 100:
    num = (a // 10) % 10
    num1 = (a // 1) % 1
    num1 = (num1 * 10) + num
    print(num1)
else:
    print("Введите двух значное число!!!!!!!!!!!!!!!!!!!!!")
    
    
    
x1, y1, x2, y2, x3, y3 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()),
if x1 < 0:
    print(X1 * -1)
elif y1 < 0:
    print(y1 * -1)
elif x2 < 0:
    print(X1 * -1)
elif y2 < 0:
    print(X1 * -1)
elif x3 < 0:
    print(X1 * -1)
elif y3 < 0:
    print(X1 * -1)   
else:
    print("отстань")

    
    
    
    
a = int(input("Введите 2-х значное число = "))
if 9 < a < 100:
    num = (a // 10) % 10
    num1 = (a // 1) % 10
    print("Кол-во десятков = ",   num)
    print("Кол-во десятков = ",  num1)
else:
    print("Неправильное число")
    
    
    
a, b, c = int(input("Введите дециметры = ")),int(input("Введите сантиметры = ")),int(input("Введите милиметров = "))
print(a / 10, "м")
print(b / 100, "м")
print(c / 1000, "м")