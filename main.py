from random import randint

n = int(input("Введите количество элементов в массиве"))
x = int(input("Укажите число X"))
arr = []

def fillArr(n): 
    for i in range(n):
        arr.append(randint(0, 10))


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# def calc(array, numb) :
#     val = 0 
#     for i in range(len(array)) :
#         if(array[i] == numb) :
#             val +=1
#     return val

# fillArr(n)
# print(arr)
# print(f"Введенное Вами число {x} найдено в массиве {calc(arr, x)} раз")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

# def search(array, numb, length) :
#     mindiff = abs(numb - array[0])
#     index = 0
#     for i in range(1, length) :
#         calc = abs(numb - array[i])
#         if(calc < mindiff) :
#             mindiff = calc
#             index = i
#     return array[index]

# fillArr(n)
# print(arr)
# print(f"Вы указали число X={x}. самый близкий по величине элемент к заданному числу является число {search(arr, x, n)}")