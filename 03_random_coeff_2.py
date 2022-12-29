# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k.'

import random
k = int(input('Введите максимальную степень: '))
coef = {}

for i in range(k, -1, -1):
    coef[i] = random.randint(-100,100)
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
    elif v == -1:
        str_equation = str_equation[:-2]
        if k == 0:
            str_equation += f'- 1 + '
        elif k == 1:
            str_equation += f'- x + '
        else:
            str_equation += f'- x**{k} + '
    elif v < -1:
        str_equation = str_equation[:-2]
        if k == 0:
          str_equation += f'- {v*(-1)} + '
        elif k == 1:
            str_equation += f'- {v*(-1)}*x + '
        else:     
            str_equation += f'- {v*(-1)}*x**{k} + '
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
