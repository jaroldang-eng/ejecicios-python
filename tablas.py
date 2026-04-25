# Función para imprimir la tabla de multiplicar
def tabla(n, hasta=10):
    print(f"\nTabla del {n}:")
    for i in range(1, hasta + 1):
        print(f"{n} x {i} = {n * i}")


# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    
    # Solo probamos hasta la raíz cuadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Función para imprimir tablas de números primos
def tablas_primos(limite):
    for num in range(2, limite + 1):
        if es_primo(num):
            tabla(num)


# Ejemplo de uso
tablas_primos(10)