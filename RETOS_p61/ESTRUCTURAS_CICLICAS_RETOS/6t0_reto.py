#!/usr/bin/python3
"""
Leer un numero natural n,
leer otro dato de tipo real x y calcular x ** n
"""
from Excepciones.main import MiError

natural = int((input("ingresa un número natural :\t")))
real = float((input("ingresa un número real :\t")))


def real_natural(real, natural):
    potencia = 0
    if natural >= 0:
        potencia = real ** natural
        result = [numero for numero in range(int(potencia) + 1)]
    else:
        # levanto mi error personalizado
        raise MiError(natural)
    return result


print(real_natural(real, natural))
