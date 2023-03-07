from math import *
a, b, c= float(input("выс = ")), float(input("низ = ")), float(input("верх = "))
ma = max(b, c)
mi = min(b, c)
l = (ma - mi) / 2
v = sqrt((l**2) +(a**2))
print(v + v +b + c)