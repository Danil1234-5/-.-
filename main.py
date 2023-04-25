#13
num = int(input())
count = 0
total = 1
for _ in range(num + 1):
    count += total
    total *= -1/2
print(count)


#9
num = int(input("Введите число больше 200 "))
if num > 200:
    for i in range(200, num + 1):
        if i % 7 == 0:
            print(i)
            break
else:
    print("Введите число больше 200")
    
    
#10
num = int(input())
if num % num == 1 and num > 600:
    for i in range(600, num + 1):
        if i % 28 == 0:
print(i)
