def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)
def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')
draw_box() 
draw_triangle()  
