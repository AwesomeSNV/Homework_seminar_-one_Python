#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_num = int(input('Введите номер четверти: '))

if quarter_num == 1:
    print('X > 0; Y > 0')
elif quarter_num == 2:
    print('X < 0; Y > 0')
elif quarter_num == 3:
    print('X < 0; Y < 0')
elif quarter_num == 4:
    print('X > 0; Y < 0')
else:
    print('Такой четверти не существует!')