# https://drive.google.com/file/d/1f-lCt1ikxJ_2XzeTgxhSVfu3nc8JeB1n/view?usp=sharing

# Задача №7 По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник
# существует, то определить, является ли он разносторонним, равнобедренным или
# равносторонним.

print('Введите длины 3-x отрезков ')

a = int(input('Длина первого отрезка: '))
b = int(input('Длина второго отрезка: '))
c = int(input('Длина третьего отрезка: '))


if a == b and b == c:
    print('Ура! Ваши отрезки создали равносторонний треугольник')
else:
    if (a == b and (a + b) > c) or (c == b and (c + b) > a) or (a == c and (a + c) > b):
        print('Ура! Ваши отрезки создали равнобедренный треугольник')
    else:
        if ((a + b) > c) and ((c + b) > a) and ((a + c) > b):
            print('Ура! Ваши отрезки создали разносторонний треугольник')
        else:
            print('Из Ваших отрезков создать треугольник невозможно"')
