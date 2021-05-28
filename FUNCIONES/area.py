#!/usr/bin/python3
from math import pi


def rectangulo(b, h):
    return b * h


def circulo(r):
    return pi * r ** 2


def total_area():
    total = rectangulo(5, 10) + circulo(3) * 2
    return total


print(total_area())
