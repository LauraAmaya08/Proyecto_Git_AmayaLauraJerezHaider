def opc():
    try:
        opc= int(input("Ingresa el numero de opcion correspondiente: "))
        return opc
    except Exception:
        error= "Valor invalido"
        print (error)
        return -1