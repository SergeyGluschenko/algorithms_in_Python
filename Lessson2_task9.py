# https://drive.google.com/file/d/1t_nbfNUECXxMviN4KPvEnjDqqEBmbP7c/view?usp=sharing

# Задача №9 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


sum_max = 0
num_max = 0
while True:
    num = int(input('Введите число для подсчета суммы цифр: '))
    b = num  # Временная переменная
    if b > 0:
        sum_num = 0
        while b > 0:
            i = b % 10
            sum_num += i
            b = b // 10
        if sum_num > sum_max:
            sum_max = sum_num
            num_max = num
    else:
        break

print(f'У числа {num_max} сумма цифр max и ровна {sum_max}')
