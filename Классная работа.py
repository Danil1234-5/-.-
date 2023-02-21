a, b = input(), input()
if a == 'красный':
    if b == a:
        print('красный')
    elif b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if b == a:
        print('синий')
    elif b == 'желтый':
        print('зеленый')
    elif b == 'красный':
        print('фиолетовый')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if b == a:
        print('желтый')
    elif b == 'красный':
        print('оранжевый')
    elif b == 'синий':
        print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')