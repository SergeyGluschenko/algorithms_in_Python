# https://drive.google.com/file/d/1t_nbfNUECXxMviN4KPvEnjDqqEBmbP7c/view?usp=sharing

# Задача №8 Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются
# вводом с клавиатуры.

q = int(input('Введите количество элементов числового ряда: '))
a = int(input('Введите искомую цифру в числовом ряду: '))

iterator = 0
count = 0
while iterator < q:
    b = int(input(f'Введите число для поиска в нем цифры {a}: '))
    if b > 0:
        while b > 0:
            i = b % 10
            if i == a:
                count += 1
            b = b // 10
    iterator += 1

print(f'Цифра {a} встретилась {count} раз в {q} числах')


