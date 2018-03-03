#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import lib

# Создайте функции:
# *генерации двумерного массива случайных чисел с заданными размерами
# *поиска максимальныъ чисел в каждой строке двумерного массива(2 функции)
# *проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int

# Поместите полученные функции в отдельный модуль. Итоговую программу оформите в отдельном модуле(файле).
# Создайте двумерный массив 10х10 из случайных чисел.Ввод размера массива сделать с клавиатуры.
# Вычислить максимальный элемент в каждой строке массива и вывести полученный список на экран.

l_string = input('Введите размер массива по вертикали: ')
l_int, ok = lib.to_int(l_string)
if not ok:
    print("Вы ввели не число")
    exit()
m_string = input('Введите размер массива по горизонтали: ')
m_int, ok = lib.to_int(m_string)
if not ok:
    print("Вы ввели не число")
    exit()

array = lib.create_array(l_int, m_int)
mas_values = lib.find_max_in_rows(array)
print(mas_values)