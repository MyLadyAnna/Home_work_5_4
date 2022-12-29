# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
k = int(input('Введите максимальную степень: '))
coef = {}

for i in range(k, -1, -1):
    coef[i] = random.randint(0,100)
print(coef)

str_equation = ''
for k,v in coef.items():
    if v == 0:
        str_equation += f''
    elif v == 1:
        if k == 0:
            str_equation += f'1 + '
        elif k == 1:
            str_equation += f'x + '
        else:
            str_equation += f'x**{k} + '
    else:
        if k == 0:
          str_equation += f'{v} + '
        elif k == 1:
            str_equation += f'{v}*x + '
        else:     
            str_equation += f'{v}*x**{k} + '
else:
    str_equation = str_equation[:-3]
print(str_equation)


my_file = open('file.txt', 'w')     
my_file.write(str_equation) 
my_file.close()              