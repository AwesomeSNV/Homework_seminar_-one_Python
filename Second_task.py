#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

#Methods

def input_numbers(x):
    xyz = ['x','y','z']
    num = []
    for i in range(x):
        num.append(input(f'Введите значение {xyz[i]}: '))
    return num

def predicate_check(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result

numbers = input_numbers(3)
if predicate_check(numbers) == True:
    print('Утверждение истинно.')
else:
    print('Утверждение ложно.')


