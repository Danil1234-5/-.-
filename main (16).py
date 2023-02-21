a = int(input())
num = a // 100
num0 = (a // 10) % 10
num1 = (a // 1) % 10
num1 = num1 *100
num0 = num0 * 10
c = num1 + num0 + num
print(a - c)