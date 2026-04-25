def celsius_a_fahrenheit(c):
    return (9/5) * c + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9


def celsius_a_kelvin(c):
    return c + 273.15


def convertir(valor, origen, destino):
    if origen == 'C' and destino == 'F':
        return celsius_a_fahrenheit(valor)

    elif origen == 'F' and destino == 'C':
        return fahrenheit_a_celsius(valor)

    elif origen == 'C' and destino == 'K':
        return celsius_a_kelvin(valor)

    elif origen == 'F' and destino == 'K':
        c = fahrenheit_a_celsius(valor)
        return celsius_a_kelvin(c)

    elif origen == 'K' and destino == 'C':
        return valor - 273.15

    elif origen == 'K' and destino == 'F':
        c = valor - 273.15
        return celsius_a_fahrenheit(c)

    else:
        return None


# PRUEBAS
print(convertir(25, 'C', 'F'))  # 77.0
print(convertir(77, 'F', 'C'))  # 25.0
print(convertir(0, 'C', 'K'))   # 273.15
print(convertir(32, 'F', 'K'))  # 273.15