# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

# Input:       5
# Output:    120

n = int(input('Введите целое число: '))
while n < 0:
    print('Введены неверные данные')
    n = int(input('Введите целое НЕ отрицательное число: '))

def FactorialNumber(number):
    if number == 0:
        factorial_number = 1
    i = 1
    factorial_number = 1
    while i <= number:
        factorial_number = factorial_number * i
        i += 1
    return factorial_number

print(FactorialNumber(n))
