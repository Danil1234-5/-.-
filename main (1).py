#Циклы с параметром
a = int(input())
print(a * 25.4 / 10)

a = int(input())
print(a *80)

e = 2.7
for i in range(1, 21):
    print(e**i)
    
a = 1.1
for i in range(0, 21):
    print(a + i)

a = 2.1
for _ in range(8):
    a += 0.1
    print(a)
    
s = 0
for i in range(100):
    if i % 2 == 0 and s < 20:
        s += 1
        print(i)

s = 0
for i in range(100):
    if i % 2 != 0 and s < 20:
        s += 1
        print(i)
        
from math import *
for i in range(2, 21):
    if i % 2 == 0:
        print(sqrt(i))
        
a = float(input("Цена конфет за 1 кг:"))
for i in range(2,11):
    print(i, "кг стоит", i * a)
      
a, b = int(input()), int(input())
for y in range(a, b + 1):
    print("x =",  y**2)  
    
a, b = int(input()), int(input())
for y in range(a, b + 1):
    x = 1/(2*y)
    print(x)
    
a, b = int(input()), int(input())
e =2.7
for x in range(a, b + 1):
    y = e**x - 1
    print(y)
    
a, b = int(input()), int(input())
for x in range(a, b + 1):
    y = (x - 1)**2
    print(y)
    
for x in range(1,20):
    t = x + 1 
    y = 2 * t ** 2 + 2 * t + 2
    print(y)
    
for x in range(2,20):
    if x % 2 == 0:
        f = 2*x 
        z = 8*f**3 - f
        print(z)
#Циклы с условием

        
        
        
        
        
        
        
        
        
        
        
        