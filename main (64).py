a = int(input())
years = int(input())
def bank(a, b):
    while b > 0:
        a *= 1.1
        b -= 1
    print(a)    
bank (a, years)