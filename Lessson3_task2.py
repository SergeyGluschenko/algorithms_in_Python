from random import randint

# Задача №2 Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

len_array = 10
min_item = 0
max_item = 100

array = [randint(min_item, max_item) for _ in range(len_array)]
print(array)
array_index_even = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        array_index_even.append(i)

print(f'Четные элементы массива стоят на позициях с индексами {array_index_even}')


