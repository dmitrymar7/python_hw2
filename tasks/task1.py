# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_of_numbers(number):
    if number == 0:
        return 0

    return number % 10 + sum_of_numbers(number // 10)

def f1_1():
    try:
        n = float(input("Введите вещественное число: "))
    except ValueError:
        print("Введено не число")
        return
    n_int = int(n)
    while n_int * 10 < int(n * 10):
        n *= 10
        n_int = int(n)
    print(sum_of_numbers(n_int))

#Функция не используется, написана в качестве альтернативы
def f1_2():
    n = input("Введите вещественное число: ")
    sum_n = 0
    for i in n:
        if i.isdigit():
            sum_n += int(i)
    print(sum_n)

f1_1()