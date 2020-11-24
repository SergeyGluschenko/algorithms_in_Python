# https://drive.google.com/file/d/1f-lCt1ikxJ_2XzeTgxhSVfu3nc8JeB1n/view?usp=sharing

# Задача №6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква


number = int(input('Введите номер буквы в алфавите от 1 до 26: '))

l = chr(number + 96)

print(f'Под номером {number} в английском алфавите стоит буква "{l}"')
