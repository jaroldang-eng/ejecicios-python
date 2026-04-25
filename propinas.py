# ---------------- FUNCIONES ----------------

def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


def calcular_total(subtotal, propina):
    return subtotal + propina


def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: número de personas inválido"
    return total / personas


def aplicar_descuento(subtotal, descuento_pct):
    return subtotal - (subtotal * (descuento_pct / 100))


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Calcular propina")
    print("2. Dividir cuenta")
    print("3. Aplicar descuento + propina")
    print("4. Salir")
    print("5. Resumen")


# ---------------- MAIN ----------------

def main():
    historial = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        # OPCIÓN 1
        if opcion == "1":
            try:
                subtotal = float(input("Subtotal: "))
                print("Sugerencias: 10%, 15%, 20%")
                porcentaje = float(input("Porcentaje: "))

                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)

                print(f"Propina: Q{propina:.2f}")
                print(f"Total: Q{total:.2f}")

                historial.append(f"Propina -> Total: Q{total:.2f}")

            except:
                print("Error: ingresa números válidos")

        # OPCIÓN 2
        elif opcion == "2":
            try:
                total = float(input("Total de la cuenta: "))
                personas = int(input("Número de personas: "))

                resultado = dividir_cuenta(total, personas)

                print(f"Cada persona paga: {resultado}")

                historial.append(f"Dividir -> {resultado}")

            except:
                print("Error: datos inválidos")

        # OPCIÓN 3
        elif opcion == "3":
            try:
                subtotal = float(input("Subtotal: "))
                descuento = float(input("Descuento (%): "))
                porcentaje = float(input("Propina (%): "))

                nuevo_subtotal = aplicar_descuento(subtotal, descuento)
                propina = calcular_propina(nuevo_subtotal, porcentaje)
                total = calcular_total(nuevo_subtotal, propina)

                print(f"Subtotal con descuento: Q{nuevo_subtotal:.2f}")
                print(f"Propina: Q{propina:.2f}")
                print(f"Total final: Q{total:.2f}")

                historial.append(f"Descuento+Propina -> Q{total:.2f}")

            except:
                print("Error: datos inválidos")

        # OPCIÓN 5 (BONUS)
        elif opcion == "5":
            print("\n--- HISTORIAL ---")
            if not historial:
                print("No hay operaciones aún")
            else:
                for item in historial:
                    print("-", item)

        # SALIR
        elif opcion == "4":
            print("¡Gracias por usar el programa! 👋")
            break

        else:
            print("Opción inválida")


# Ejecutar programa
main()