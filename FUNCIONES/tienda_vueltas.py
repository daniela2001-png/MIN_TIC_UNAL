#!/usr/bin/python3
"""
Mi mamà me manda a comprar P panes a $ 300 cada uno, M bolsas
de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
programa que me diga las vueltas (o lo que quedo debiendo) cuando
me da un billete de B pesos.
"""


def vueltas(billete, P, M, H):
    precio_pan = (P * 300) or 0
    precio_leche = (M * 3300) or 0
    precio_huevos = (H * 350) or 0
    total_pagar = precio_huevos + precio_leche + precio_pan
    total_vueltas = billete - total_pagar
    return f"Sus vueltas son: ${total_vueltas} pesos en total"
