# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num=int(input('Введите число k: '))
fibo_l = list()
fibo_l.append(0)
fibo_l.append(1)
for i in range(2, num + 1):
    fibo_l.append(fibo_l[i - 1] + fibo_l[i - 2])

fibo_l.insert(0, 1)
fibo_l.insert(0, -1)
for i in range(0, num - 2):
    fibo_l.insert(0, (fibo_l[1]) - (fibo_l[0]))

print(f'для k = {num} списко будет выглядеть так: {fibo_l}')









