#!/usr/bin/python3
"""
Imprimir los n ́umeros pares en forma descendente hasta 2 que son
menores o iguales a un n ́umero natural n ≥ 2 dado.
"""


def pares(num):
    lista = [n for n in range(num, 3, 2)]
    return lista


num = int(input("ingrese un numero: "))
print("Los numeros pares menores o igual a dos según el número dado son: {}".format(pares(num)))
