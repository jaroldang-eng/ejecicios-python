def calcular_billetes(monto):
    if monto % 20 != 0:
        print("Error: el monto debe ser múltiplo de 20")
        return None

    b200 = monto // 200
    monto = monto % 200

    b100 = monto // 100
    monto = monto % 100

    b50 = monto // 50
    monto = monto % 50

    b20 = monto // 20

    print(b200, b100, b50, b20)


calcular_billetes(480)
calcular_billetes(1000)
