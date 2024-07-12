from funciones import*
from menu import*
from interaccionJson import*

datos = cargar ("baseDatos.json") 

while True:
    menu_principal()
    opcion= opc()
    while opcion not in [1,2,3,4]:
        opcion =opc()
        print("Ingresa una opcion valida\n")
    if opcion==1:
            menu_VerCiudad()
            opcion =opc()
            while opcion not in [1,2,3]:
                opcion =opc()
                print("Ingresa una opcion valida\n")
            if opcion==1:
                print("mostrar json")
            elif opcion==2:
                    menu_Buscar()
                    while opcion not in [1,2,3,4]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
                    if opcion==1:
                            print("buscar por nombre")
                    elif opcion==2:
                            print("buscar por pais")
                    elif opcion==3:
                            print("buscar por codigo postal")
                    else:
                        print("SALISTE DE BUSCAR CIUDAD")
    elif opcion==2:
        print("funcion añadir ciudad")
    elif opcion==3:
        print("si")
    else:
        print("MUCHAS GRACIAS POR USAR CITY LOCATION")
        exit()

































datos = guardar (datos,"baseDatos.json")