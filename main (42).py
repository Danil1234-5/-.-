def sum_and_umnojenie():
    a = int(input())
    if 999 < a < 10000:
        num = a // 1000
        num1 = (a % 1000) // 100
        num2 = (a % 100) // 10
        num3 = a % 10 
        print(num + num1 + num2 + num3, num * num1 * num2 * num3 )
    else:
        print("Неверное число")
sum_and_umnojenie()

def Celoe_piat():
    a = int(input())
    if 10 <= a < 100000:
        num = (a % 100) // 10
        num1 = a % 10
        print(num, num1)
    else:
        print("Неправильное число")
Celoe_piat()

def raznocti():
    a = int(input())
    if 99 < a < 1000:
        num = a // 100
        num1 = (a % 100) // 10
        num2 = a % 10
        f = num
        c = num1 * 10
        v = num2 * 100
        popit = f + c + v
        print(a - popit)
    else:
        print("НЕверно число")
raznocti()

def n_chislo():
    a = int(input())
    if 0 <= a:
        b = len(str(a))
        while a > 0:
            num = a // 10 ** (b-1)
            print(num)
            a %= 10 **(b-1)
            b -= 1
n_chislo()

def in_zapic_2():
    a = input()
    if "2" in a:
        print("Входит")
    else:
        print("Не входит")
in_zapic_2()




