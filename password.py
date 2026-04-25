def validar_password(password):
    if len(password) < 8:
        print("Contraseña muy corta")
        return

    tiene_mayuscula = False
    tiene_numero = False

    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True

    if tiene_mayuscula and tiene_numero:
        print("Contraseña válida")
    else:
        print("Contraseña inválida")


validar_password("Hola1234")