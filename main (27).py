#Меньше P
from math import *
P = int(input())
for i in range(2, P + 1):
    if P > sqrt(i):
        print(sqrt(i))
        
        
#Все числа между А и В
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if a < i < b:
        print(i)
        
        
        
#Все числа между А и В
a, b = int(input()), int(input())
for i in range(b, a, - 1):
    if a < i < b:
        print(i)
        
        
        
#hf,jnf c n
a = int(input())
k = int(input())
for i in range(1, a + 1):
    if 3*k > i:
        print(k)
        print(3*k)
        break





























