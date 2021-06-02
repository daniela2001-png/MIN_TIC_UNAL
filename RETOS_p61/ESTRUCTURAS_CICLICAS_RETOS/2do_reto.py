#!/usr/bin/python3
"""
Imprimir un listado con los n ́umeros impares desde 1 hasta 999 y
seguidamente otro listado con los n ́umeros pares desde 2 hasta 1000.
"""


def impar_par():
    # impares = [(n + 1) for n in range(1, 1000)]
    pares = [x for x in range(1, 1000) if x % 2 == 0]
    impares = [y for y in range(2, 1001) if y % 2 != 0]
    return f"pares : {pares}\n\n\n impares : {impares}"
