#!/usr/bin/python3
"""
Calcular el valor de 2 elevado a la potencia n
"""


def potencia(n):
    result = [2 ** i for i in range(n + 1)]
    return result


print(potencia(2))
