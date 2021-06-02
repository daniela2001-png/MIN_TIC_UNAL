#!/usr/bin/python3
"""
Imprimir un listado con los numeros del 1 al 100 cada uno con su
respectivo cuadrado.
"""


def cuadrado():
    cuadrados = [n ** 2 for n in range(1, 101)]
    return cuadrados
