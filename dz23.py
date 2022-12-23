# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list= [2, 3, 4, 5, 6]
x_list=[]
len_x=len(my_list)
if (len_x/2)%2==0:
    pol_len_x=int(len_x/2)
    print(len_x)
    for i in range(pol_len_x):
        x_list.append(int(my_list[i])*int(my_list[len_x-1]))
        len_x-=1
else:
    pol_len_x=int((len_x/2)+1)
    for i in range(pol_len_x):
        if i == (len_x-1):
            x_list.append(int(my_list[i])*2)
            break
        else:
            x_list.append(int(my_list[i])*int(my_list[len_x-1]))
            len_x-=1

print(f'{my_list}-> ответ: {x_list}')