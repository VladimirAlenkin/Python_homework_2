# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь
# вводит с клавиатуры.

print('Введите количество монет>? ', end="")
quantity = int(input())
 
countZero = 0
countOne = 0
#temp = 0
for i in range (quantity):
    print('Положение монеты ' , i, ': 0 или 1>? ', end="")
    temp = int(input())
    
    if temp == 0:
        countZero += 1
    else:
        countOne += 1
   
 
min = countZero if countZero <= countOne else countOne
print('Количество монет, чтобы перевернуть: ', min)
#print (countOne, countZero)

#решено
