# 5 Реализуйте алгоритм перемешивания списка.

from random import randint

def shuffle_list(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        index = randint(0, len_lst - 1)
        temp = lst[index]
        lst[index] = lst[i]
        lst[i] = temp

def f5():
    lst = input("Введите элементы списка: ").split()
    print(f"Исходный список: {lst}")
    shuffle_list(lst)
    print(f"Перемешанный список: {lst}")

f5()
