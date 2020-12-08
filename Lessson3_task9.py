from random import randint

# Задача №9 Найти максимальный элемент среди минимальных элементов столбцов матрицы.

col_array = 4
line_array = 5
min_item = 0
max_item = 100
array = [[randint(min_item, max_item) for _ in range(col_array)] for _ in range(line_array)]


for line in array:   # вывод матрицы красиво
    sum_line = 0
    for i, item in enumerate(line):
        print(f'{item:>6}', end='')
    print(end='\n')

print('*' * 100)

for i in range(len(array[0])):  # находим минимальные значения в столбцах
    min_num = array[0][i]
    for line in range(len(array)):
        if min_num > array[line][i]:
            min_num = array[line][i]
    print(f'{min_num:>6}', end='')
    if i == 0:                         # на первой итерации минимально число в колонке будет и максмальным в матрице
        max_from_min = min_num
    elif min_num > max_from_min:
        max_from_min = min_num

print(f'   минимальные в столбцах, а максимальный среди них {max_from_min}')
