#!/usr/bin/python3
"""
Imprimir los n ́umeros de 1 hasta un n ́umero natural n dado, cada uno
con su respectivo factorial.
"""


def factorial(n):
    if (n <= 1):
        return 1
    else:
        return factorial(n-1) * n


print("su factorial es: ", factorial(int(input("ingrese un numero: "))))
