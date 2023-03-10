# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза.

# Input:	5 -> 5 1 6 5 9
# Output:	1 9

import random

n = int(input('Введите число: '))

numb = random.randint(1,9)
print(f'1 арбуз весит - {numb}')
min1 = numb
max1 = numb

for i in range(2, n + 1):
    numb = random.randint(1,9)
    print(f'{i} арбуз весит - {numb}')
    if numb > max1:
        max1 = numb
    elif numb < min1:
        min1 = numb

print(f'\n Минимальная масса: {min1}  Максимальная масса: {max1}')