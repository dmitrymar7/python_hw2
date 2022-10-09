# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

def f1():
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Введено не целое число")
        return
    lst = [factorial(i) for i in range(1, n + 1)]
    print(lst)
f1()
