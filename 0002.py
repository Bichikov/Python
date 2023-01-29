# Найдите сумму цифр трехзначного числа : 123 --> 6 (1+2+3)

a = int (input('Введите трехзначное число'))
summa = 0 

while a > 0 :
    ost = a % 10
    summa += ost
    a = a // 10

else :
    print (summa)

     