def ejercicio_diccionario():
    alumno = {
        "nombre": "Javier",
        "edad": 20,
        "ciudad": "Guatemala",
        "lenguaje_favorito": "Python"
    }

    # Agregar universidad
    alumno["universidad"] = "USPG"

    # Modificar edad
    alumno["edad"] = 21

    # Imprimir con items()
    for clave, valor in alumno.items():
        print(clave, ":", valor)

    # Verificar email
    print("¿Existe email?", "email" in alumno)

    # Obtener telefono sin error
    print("Teléfono:", alumno.get("telefono", "No existe"))

ejercicio_diccionario()