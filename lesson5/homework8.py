import random

# Задание 1
#Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив, содержащий отсортированные числа от 10 до 250 млн.
# Можно использовать функцию randomint из модуля random для ещё большей рандомизации значений,
# но для целей работы алгоритма бинарного поиска проследите, чтобы значения в массиве были отсортированы

an_cnt = 0
fr_ar = range(10, 250, 5)



# Задание 2
#Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.
cnt = 0
usr_list = []

while (cnt< 10):
    usr_list.append(random.randint(10, 250))
    cnt +=1

usr_list.sort()



# Задание 3
# Напишите функцию для алгоритма линейного поиска.


#test_ar = [1, 2, 67, 98, 100, 109, 110, 201, 223, 300]

def serch_dig_line(dig, ar_dig):
    cnt_ar = 0
    for i in ar_dig:
        if i == dig:
            cnt_ar += 1

    if cnt_ar == 1:
        print(f"Число {dig} найдено")
    else:
        print(f"Число {dig} не найдено")



def serch_dig_bin(dig, ar_dig):
    left = 0
    right = len(ar_dig) - 1
    fnd = False
    while(left < right):
        middle = int((left + right)/2)
        if ar_dig[middle] == dig:
            fnd = True
            break
        elif ar_dig[middle] > dig:
            right = middle - 1
        elif ar_dig[middle] < dig:
            left = middle + 1
    if ar_dig[left] == dig:
        fnd = True

    if fnd == True:
        print(f"Число {dig} найдено")
    else:
        print(f"Число {dig} не найдено")





for i in usr_list:
    serch_dig_bin(i, fr_ar)

for i in usr_list:
    serch_dig_line(i, fr_ar)