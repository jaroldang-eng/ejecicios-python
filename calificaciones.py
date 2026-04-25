notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]

def promedio(notas):
    suma = 0
    for n in notas:
        suma += n
    return suma / len(notas)


def mayor(notas):
    m = notas[0]
    for n in notas:
        if n > m:
            m = n
    return m


def menor(notas):
    m = notas[0]
    for n in notas:
        if n < m:
            m = n
    return m


def contar_aprobados(notas, minimo=61):
    contador = 0
    for n in notas:
        if n >= minimo:
            contador += 1
    return contador


def reporte(notas):
    print("Promedio:", promedio(notas))
    print("Mayor:", mayor(notas))
    print("Menor:", menor(notas))
    print("Aprobados:", contar_aprobados(notas))


reporte(notas)