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
                  while True:
                        menu_VerCiudad()
                        while opcion not in [1,2,3]:
                            opcion =opc()
                            print("Ingresa una opcion valida\n")
                        if opcion==1:
                              print("mostrar json")
                        elif opcion==2:
                              while True:
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
                                     break
                        else:
                             print("SALISTE DE BUSCAR CIUDAD")
                             break
            elif opcion==2:
                 print("funcion añadir ciudad")
            elif opcion==3:
                while True:
                    menu_Actualizar()
                    while opcion not in [1,2,3,4,5]:
                        opcion =opc()
                        print("Ingresa una opcion valida\n")
                    if opcion==1:
                         print("actualizar el nombre")
                    elif opcion==2:
                         print("actualizar codigo postal")
                    elif opcion==3:
                         print("actualizar la poblacion")
                    elif opcion==4:
                         print("actualizar pais")
                    else:
                        print("SALISTE DE ACTUALIZAR")
            else:
                 print("MUCHAS GRACIAS POR USAR CITY LOCATION")
                            
                                
                                     


































datos = guardar (datos,"baseDatos.json")