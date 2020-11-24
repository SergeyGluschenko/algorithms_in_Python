# https://drive.google.com/file/d/1f-lCt1ikxJ_2XzeTgxhSVfu3nc8JeB1n/view?usp=sharing

# Задача №8 Определить, является ли год, который ввел пользователем, високосным или не високосным.

y = int(input('Введите года: '))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(f'{y} високосный год')
        else:
            print(f'{y} не високосный год')
    else:
        print(f'{y} високосный год')
else:
    print(f'{y} не високосный год')
