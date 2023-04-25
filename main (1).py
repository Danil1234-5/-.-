#11
kilometr = 10
day = 0
while kilometr < 20:
    kilometr += kilometr * 0.1
    day += 1
print(day)

#12
num = int(input())
y = 0
for i in range(1, num + 1):
    y += ((2*num) - 1) / (2*num)
print(y)

#14
num = int(input())
if num < 100:
    for i in range(1, num + 1):
        if i % 11 == 0:
            print(i)
            i += 1
        