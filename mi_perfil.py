# mi_perfil.py

def main():
    print("=== Registro de Perfil ===")

    # Solicitar datos al usuario
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    ciudad = input("Ingresa tu ciudad: ")
    hobby = input("Ingresa tu hobby: ")

    # Mostrar tarjeta de presentación
    print("\n--- Tarjeta de Presentación ---")
    print(f"Nombre : {nombre}")
    print(f"Edad   : {edad}")
    print(f"Ciudad : {ciudad}")
    print(f"Hobby  : {hobby}")
    print("--------------------------------")


# Ejecutar el programa
if __name__ == "__main__":
    main()
