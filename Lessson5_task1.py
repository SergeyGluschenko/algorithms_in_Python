from collections import deque
# Задача№5_1 Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

avg = 0
firm = {}
corrector_range = 1
quantity_quarters = 4
quantity_firm = int(input("Количество предприятий: "))
profit_total = 0
for i in range(quantity_firm):
    firm_name = input(f'Введите название {i+ corrector_range} фирмы: ')
    firm_profit = 0
    for i in range(quantity_quarters):
        profit = int(input(f'Введите прбыль фирмы {firm_name} за {i + corrector_range} -й квартал: '))
        firm_profit += profit

    firm[firm_name] = firm_profit
    profit_total += firm_profit
    print(firm)

avg = profit_total / quantity_firm

Lider_firm = []
Loser_firm = []

print(f'Средняя прибыль за год для всех предприятий ровна: {avg}')
for i in firm:
    if firm[i] > avg:
        Lider_firm.append(i)
    else:
        Loser_firm.append(i)

print(f'Прибыль больше среднего: {Lider_firm}')
print(f'Прибыль меньше среднего: {Loser_firm}')
