#!/usr/bin/python3
numero_1er_semestre = int(
    input("Digita el número de estudiantes de primer semestre: "))


def numero_estudiantes():
    numero_2do_semestre = 2 * (numero_1er_semestre) + 4
    numero_3er_semestre = (numero_1er_semestre + numero_2do_semestre) / 5
    # Si el tercer semestre está entre 0 y 20, debe imprimir la palabra uno.
    rango_er_semestre = "cuatro"
    if (numero_3er_semestre >= 0 and numero_3er_semestre <= 20):
        rango_er_semestre = "uno"
    # Si el tercer semestre está entre 21 y 30, debe imprimir la palabra dos.
    elif (numero_3er_semestre >= 21 and numero_3er_semestre <= 30):
        rango_er_semestre = "dos"
    #  Si el tercer semestre está entre 31 y 50, debe imprimir la palabra tres.
    elif (numero_3er_semestre >= 31 and numero_3er_semestre <= 50):
        rango_er_semestre = "tres"
    return f"{numero_1er_semestre} {numero_2do_semestre} {int(numero_3er_semestre)} \
    \n{rango_er_semestre}"


print(numero_estudiantes())
