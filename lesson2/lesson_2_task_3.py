# Напишите функцию square, принимающую один аргумент — сторону квадрата — и возвращающую площадь квадрата.
# Если переданный аргумент был не целым, округлите результат вверх.

from math import ceil
a = float(input("Введи сторону квадрата: \n"))
b = ceil (a)
def square (b):
    print ("Площадь квадрата =", b*b)
square (b)