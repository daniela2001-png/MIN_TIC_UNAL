#!/usr/bin/python3
def ord_f(letra):
    try:
        if len(letra) == 1:
            ord(letra)
        else:
            return "len igual a 1"
    except TypeError:
        return "solo strings "
