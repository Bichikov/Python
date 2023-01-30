# Найдите сумму цифр трехзначного числа : 123 --> 6 (1+2+3)
a = int (input('Введите  число: '))
while a > 999 or a < 100:
    a = int (input('Введите 3-ое число: '))

a1 = a
summa = 0 

while a > 0 :
    ost = a % 10
    summa += ost
    a = a // 10

else :
    print (f'Сумма всех чисел в числе "{a1}" --> {summa}')

     