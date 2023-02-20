a = float(input('Веедите еженедельную прибавку: '))
b = float(input('Веедите изначальный вес: '))
c = int(input('Введите количество недель: '))

for i in range(1, c+1):
    c = b + a
    c = round(c, 3)
    print(f"{i} неделя = {c}")
    b += a