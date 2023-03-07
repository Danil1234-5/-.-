#Максимальное и минимальное
a, b = float(input()), float(input())
print("Максимальное = ", max(a, b), "Минимальное = ", min(a, b))

#Площадь кольца
r, a = float(input()), float(input())
if r == a / 2:
    print("Вписанно")
else:
    print("Не вписанно")

#Решение функции
x = float(input())
y = 0
if x < 0:
    y = x**2
    print(y)
elif x > 0:
    y = 1 / (x**2)
    print(y)
    
#Площадь кольца 2
from math import *
r, a = float(input()), float(input())
b = sqrt(a**2 + a**2)
if r == b / 2:
    print("Вписанно")
else:
    print("Не вписанно")
    
#Максимальное
a, b = float(input()), float(input())
print("Максимальное = ", max(a, b))

#Минимальное
a, b = float(input()), float(input())
print("Минимальное = ", min(a, b))

#Расстояние
a, b = float(input()), float(input())
a = a / 1000
b = b * 0.45
print("Больше = ", max(a, b))

#Функция 2
x, a = float(input()), float(input())
if x < 1:
    y = a**2 + x**2
    print(y)
elif x > 1:
    y = a**2 - x**2
    print(y)
    
#Вычисление частного
a, b = float(input()), float(input())
print("Частное а / b = ", a / b)