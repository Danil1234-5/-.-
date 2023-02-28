print("Введите 3-x значное число")
a = int(input())

if 99 < a < 1000:
    
    num1 = a // 100
    num2 = (a // 10) % 10
    num3 = (a // 1) % 10
    
    c = int(str(num3) + str(num2) + str(num1))
    

    if a == c:
        print("DA")
    else:
        print("NET")
else: 
    print("Введено не правильное число")