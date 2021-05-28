def char_f(numero):
    c = chr(numero)
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        respuesta = "es una vocal minúscula."
    else:
        respuesta = "no es una vocal minúscula."
    return f"El número introducido corresponde al carácter: {c} y {respuesta}"


print(char_f(97))
