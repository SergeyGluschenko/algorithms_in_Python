# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
import sys


def qwerty(*args):
    unique_argv = []
    for q in args:
        if q not in unique_argv:
            unique_argv.append(q)
    print(unique_argv)
    memory = 0
    for r in range(len(unique_argv)):
        memory += (sys.getsizeof(unique_argv[r]))
    return memory


# вариант 1 без "массивов"
START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

array = [START_NUM, END_NUM, START_DIV, END_DIV]

for i in range(START_DIV, END_DIV + 1):
    array.append(i)
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    array.append(frequency)
    print(f'Числу {i} кратно {frequency} чисел')

print(array)
array.append(1)
print(array)

answer = qwerty(*array)
print(f'Занято памяти в 1-м варианте => {answer}')


# вариант 2 с "массивами"

print('вариант 2')

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

array = [START_NUM, END_NUM, START_DIV, END_DIV]

frequency = [0] * (END_DIV - START_DIV + 1)
array.append(frequency)


for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency[j - START_DIV] += 1

array.append(i)
array.append(j)
array.append(1)


for _ in range(len(frequency)):
    array.append(frequency[_])


for i, item in enumerate(frequency, start=START_DIV):
    array.append(i)
    array.append(item)
    print(f'Числу {i} кратно {item} чисел')


answer = qwerty(*array)
print(f'Занято памяти в 2-м варианте => {answer}')

