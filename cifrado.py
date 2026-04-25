# Función para cifrar un carácter
def cifrar_caracter(c, desplazamiento):
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        posicion = ord(c) - base
        nueva_pos = (posicion + desplazamiento) % 26
        return chr(base + nueva_pos)
    else:
        return c

# Función para cifrar mensaje
def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

# Función para descifrar
def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

# Programa principal
mensaje = input("Escribe un mensaje: ")
desplazamiento = int(input("Desplazamiento: "))

cifrado = cifrar_mensaje(mensaje, desplazamiento)
print("Cifrado:", cifrado)

print("Descifrado:", descifrar_mensaje(cifrado, desplazamiento))