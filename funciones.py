import json

#pedir opcion
def opc():
    try:
        opc= int(input("Ingresa el numero de opcion correspondiente: "))
        return opc
    except Exception:
        error= "Valor invalido"
        print (error)
        return -1

#guardar los ciudad 
def guardarCiudad(ciudad):
    with open('baseDatos.json','w') as json_file:
        json.dump(ciudad, json_file, indent=4)

#crear ciudad 
def crear_Ciudad():
    with open("baseDatos.json","r") as json_file:
        datos = json.load(json_file)

    ciudad={}
    ciudad["nombre"]=input("INGRESE EL  NOMBRE: ")
    ciudad["codigo_postal"]=input("INGRESE EL CODIGO POSTAL: ")
    ciudad["poblacion"]=input("INGRESE LA POBLACION ESTIMADA: ")
    ciudad["pais"]=input("INGRESE EL PAIS: ")
    datos.append(ciudad)
    print("LA CIUDAD HA SIDO CREADO EXITOSAMENTE")
    guardarCiudad(datos)
    return

#mostrar ciudades
def mostrar_Ciudades():
    with open("baseDatos.json","r") as json_file:
        datos = json.load(json_file) 
        for user in datos:
            print("-----------------------------------------------------------------")
            print("nombre",":", user["nombre"])
            print("codigo_postal",":", user["codigo_postal"])
            print("poblacion",":", user["poblacion"])
            print("pais",":", user["pais"])
            print("----------------------------------------------------------------")

#editar ciudad
def editarCiudad():
    with open("baseDatos.json","r") as json_file:
        datos = json.load(json_file)

        codigo_postal =input("INGRESE EL CODIGO POSTAL DE LA CIUDAD A EDITAR: ")
        for i in range(len(datos)):
            if datos[i]["codigo_postal"] == codigo_postal:
                nuevo_nombre = input("INGRESE EL NUEVO NOMBRE DE LA CIUDAD: ")
                nuevo_codigo_postal = input("INGRESE EL NUEVO CODIGO POSTAL: ")
                nuevo_pais = input("INGRESE EL NUEVO PAIS: ")

                datos[i]["nombre"] = nuevo_nombre
                datos[i]["codigo_postal"] = nuevo_codigo_postal
                datos[i]["pais"] = nuevo_pais
                print("LA CIUDAD HA SIDO EDITADA")
                break
            else:
                print("EL DOCUMENTO NO EXISTE")
    with open("baseDatos.json", "w") as json_file:
            json.dump(datos, json_file, indent=4) # type: ignore  # noqa: F821
 