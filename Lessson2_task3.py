# https://drive.google.com/file/d/1t_nbfNUECXxMviN4KPvEnjDqqEBmbP7c/view?usp=sharing

# Задача №3 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843.


def func(a):
    if a < 10:
        return f'{a}'
    return f'{a % 10}{func(a // 10)}'


number = int(input('Введите число для преобразавания: '))

b = func(number)

print(b)
