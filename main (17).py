a = int(input())
num = a // 100000
num0 = (a // 10000) % 10
num1 = (a // 1000) % 10
num2 = (a // 100) % 10
num3 = (a // 10) % 10
num4 = (a // 1) % 10
if num == 2:
    print("2 входит")
if num0 == 2:
    print("2 входит")
if num1 == 2:
    print("2 входит")
if num2 == 2:
    print("2 входит")
if num3 == 2:
    print("2 входит")
if num4 == 2:
    print("2 входит")
else:
    print("2 не входит")