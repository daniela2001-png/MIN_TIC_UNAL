#!/usr/bin/python3
"""
Dise ̃ne un programa que muestre las tablas de multiplicar del 1 al 9.
"""


def tablas_multiplicar():
    for numero in range(1, 10):
        print(f"\nTabla del {numero}:")
        for numero2 in range(1, 10):
            print(f"{numero} x {numero2} = {numero * numero2}")
    return ""


print(tablas_multiplicar())
