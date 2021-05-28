# distancia entre dos puntos: sqrt((x1-x2)**2 + (y1-y2)**2)
# Centro del círculo: (a, b)
# Punto en el plano cartesiano: (xp, yp)
# r: radio del círculo
from math import sqrt


def delcirculo(a, b, xp, yp, r):
    d = sqrt((a-xp)**2 + (b-yp)**2)
    print("  .. está por fuera") if (d > r) else print("  .. está por dentro")


print(delcirculo(3, 3, 8, 8, 4))
