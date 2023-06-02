a = int(input())
def is_prime(a):
    if 0 < a < 1000:
        if a / 1 == a and a / a == 1  and a % 2 != 0:
            print("простое, true")
        else:
            print("сложное, false")
is_prime(a)