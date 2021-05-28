#!/usr/bin/python3
from math import pi


def calcular_volumen(r1, r2, h):
    esfera = (4/3) * pi * r1 ** 3
    cono = (1/3) * h * pi * r2 ** 2
    volumen = esfera + cono
    return volumen
