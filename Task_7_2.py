# 2) Отсортируйте по возрастанию методом слияния
# одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import random


def sort_merge(arr):
    count = len(arr)
    if count > 2:
        part_1 = sort_merge(arr[:count // 2])
        part_2 = sort_merge(arr[count // 2:])
        arr = part_1 + part_2
        last_index = len(arr) - 1

        for i in range(last_index):
            min_value = arr[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > arr[j]:
                    min_value = arr[j]
                    min_index = j

            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    elif len(arr) > 1 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]

    return arr


len_range = 8


list_test = [round(random() * 50, 2) for i in range(len_range)]
print(list_test)

r = sort_merge(list_test)
print(r)
