
import json

datos = []

def cargarlista():
    global datos
    try:
        with open("datos.json","r",encoding="utf-8") as archivo:
            datos = json.load(archivo)
        print("Lista de alumnos cargados correctamente")
    except FileNotFoundError:
        print("Todavia no se cargo ningun alumno")

def ingresar():
    dni = input("Ingrese DNI: ")
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    edad = int(input("Ingrese Edad: "))

    registro = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad
    }
    datos.append(registro)
    print("Alumno registado correctamente")

def cargarjson():
    with open("datos.json","w",encoding="utf-8") as archivo:
        json.dump(datos,archivo, indent=4)
        
    print("Alumno cargado correctamente")

def consultar():
    with open("datos.json","r",encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for dato in datos:
        print("DNI: ",dato["dni"])
        print("Nombre : ",dato["nombre"])
        print("Apellido : ",dato["apellido"])
        print("Edad : ",dato["edad"])


cargarlista()
ingresar()
cargarjson()
consultar()

    
    
    
    
    
