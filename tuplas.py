
coordenadas = (14.6349, -90.5069)  # lat, lon


lat, lon = coordenadas
print("Latitud:", lat)
print("Longitud:", lon)


def estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return (minimo, maximo, promedio)

numeros = [10, 20, 30, 40]
resultado = estadisticas(numeros)
print("Estadísticas (min, max, promedio):", resultado)


distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

print("Distancia Guate a Escuintla:", distancias[("Guate", "Escuintla")])


try:
    coordenadas[0] = 15
except TypeError as e:
    print("Error:", e)
    print("Las tuplas son inmutables, no se pueden modificar.")