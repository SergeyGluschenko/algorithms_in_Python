# 1) Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def sort_ball(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr)
        n += 1
    return arr


start_range = -100
end_range = 100
len_range = 10

list_test = [randint(start_range, end_range) for i in range(len_range)]
print(list_test)

r = sort_ball(list_test)
print(r)
