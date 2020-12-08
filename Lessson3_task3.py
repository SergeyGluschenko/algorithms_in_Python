from random import randint

# Задача №3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

len_array = 10
min_item = 0
max_item = 100
array = [randint(min_item, max_item) for _ in range(len_array)]

max_index = 0
min_index = 0
max_num = array[0]
min_num = array[0]

for i in range(len(array)):
    if array[i] > max_num:
        max_num = array[i]
        max_index = i
    elif array[i] < min_num:
        min_num = array[i]
        min_index = i

print(f'Исходный массив {array}')
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Исходный массив {array}, где поменял местами минимальный и максимальный элементы')
