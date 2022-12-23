# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec= int(input('Введите десятичное число :'))
dvoi=[]
    
while dec > 0:
    dvoi.append(str(dec % 2))
    dec //= 2
dvoi.reverse()
dvoi = list(map(int,dvoi))
print("".join(map(str,dvoi)))