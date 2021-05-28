#!/usr/bin/python3
vueltas = __import__('tienda_vueltas').vueltas
calcular_volumen = __import__('volumen_cono').calcular_volumen
covid = __import__('covid').covid
char = __import__('char').char
ord_f = __import__('ord').ord_f


print("Ejecucion modulo que calcula el volumen de un cono mas una esfera")
print(calcular_volumen(10, 5, 6))
print("Ejecucion modulo que calcula las vueltas de un mandado")
print(vueltas(1000, 2, 1, 2))
print("Ejecucion modulo que calcula el numero de contagiados por dia")
print(covid(100, 4))

print("Ejecucion modulo que retorna la letra del numero correspodiente en ascci")
print(char(120))
print("Ejecucion modulo que retorna el numero de la letra correspodiente en ascci")
print(ord('B'))
