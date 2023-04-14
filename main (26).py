#все числа меньше n
n = int(input())
counter = n
for i in range(n):
    if counter != 0:
        counter = counter - 1 
        print(i)



#алгоритм который не работает
a = int(input())
counter = 0 
for i in range(1, a + 1):
    counter = counter + 1 / i 
if counter > a:
    print(counter)   
    
    
    
#квадрат больше n
n = int(input())
for i in range(n):
    if i**2 > n:
        print(i)
        break
    
    
    
#больше 200 и делиться на 17
a = int(input())
for i in range(a):
    if i > 200 and i % 17 == 0:
        print(i)
        break
    
    
    
#меньше 600 и делится на 28
n = int(input())
max1 = max2 = 1
for i in range(1, n + 1):
    if i <= 600 and i % 28 == 0:
        if  i > max1:
            max2 = max1
            max1 = i
print(max1)