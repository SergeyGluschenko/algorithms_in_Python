# Задача №1 В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

count = 0  # счетчик кратных чисел
for a in range(2, 10):
    count = 0
    for b in range(2, 100):
        if b % a == 0:
            count += 1
    print(f'Цифре {a} в диапазоне 2..99 кратны {count} чисел')
