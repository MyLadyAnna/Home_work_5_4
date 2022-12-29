# Задача - сформировать файл, содержащий сумму многочленов.

import random

def create_equation():                              #рандомайзер коэф для степеней Х                         
    degree = int(input('Введите степень: '))
    equation = {}
    for n in range(degree, -1, -1):
        equation[n] = random.randint(-20, 20)
    return equation

def decode(equation: dict) -> str:              # из словаря в строку
    new_equation = []
    for key, value in equation.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ')\
        .replace('*x**0', '').replace(' 1*x', ' x').replace('x**1', 'x')
    if new_equation.startswith('1*x'):
        return new_equation[2:]
    elif new_equation.startswith('-1*x'):
        return new_equation[3:]
    else:
        return new_equation

def encode(equation: str) -> dict:                  # из строки в словарь
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')\
        .replace(' -x', ' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x**1 ').split()[:-2]
    dict_equation = {}
    for item in equation:
        i = item.split('*x**')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        else:
            dict_equation[0] = int(i[0])
    return dict_equation

def addition(first_eq: dict, second_eq: dict):          # сумма многочленов
    final_eq = {}
    final_eq.update(final_eq)
    final_eq.update(second_eq)
    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0)
    return final_eq

equation1 = create_equation()
print(f'Первый многочлен: {decode(equation1)}')
equation2 = create_equation()
print(f'Второй многочлен: {decode(equation2)}')
print(f'Их сумма: {addition(equation1, equation2)}')
