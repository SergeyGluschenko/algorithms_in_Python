# 3) Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint


def sort_med(arr):
    for i in range(len(arr)):
        count_less = 0
        count_more = 0
        count_same = 0
        print(f"{i}-й элемент")
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count_same += 1
            elif arr[i] > arr[j]:
                count_more += 1
            else:
                count_less += 1
        #print(count_same)
        #print(count_less)
        #print(count_more)
        #print(f'{abs(count_less - count_more)} разница')
        if abs(count_less - count_more) < count_same:
            break
    num_med = arr[i]
    return num_med


start_range = 0
end_range = 50
m = 3  # задаем переменную любым способом
len_range = 2 * m + 1

# формируем массив
list_test = [randint(start_range, end_range) for i in range(len_range)]

print(list_test)

r = sort_med(list_test)
print(f'Элемент {r} является медианой')

