# Задача №8 Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

quantity_line = 5
array = [input('Введить 3 элемента строки разделенные пробелом: ').split(' ') for _ in range(quantity_line)]

for line in array:
    sum_line = 0
    for i, item in enumerate(line):
        line[i] = int(line[i])
        sum_line += line[i]
        print(f'{item:>6}', end='')
    line.append(sum_line)

    print(f'{sum_line:>6}')  # Beautiful is better than ugly




