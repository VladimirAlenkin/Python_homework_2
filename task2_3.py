#Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

N = int(input('Введите число: '))

result = 1 # 2**0 = 1
while result < N:
    print(result, end=',')
    result *= 2

#решено
