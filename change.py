def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    cents = round((vuelto-pesos)*100)
    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n\nvuelto\n\n{pesos}\nCentavos:\n{cents}")
