import datetime 

# listas para almacenar de forma ordenada el historial de datos de cada equipo
# tuplas para los datos de cada préstamo (usuario, fecha)
# Diccionarios para almacenar todos los equipos, su estado, disponibilidad y prestamos asociados
#Funciones modulares 
#Menu interactivo 



#Estructuras de datos principales
#inventario equipos: clave es el nombre del equipo, el cual el valor es 
# otro diccionario con disponibilidad y una lista que va a contener los prestamos
inventario_equipos = {"PC gamer":{
    "disponibilidad": False,
    "prestamos": [("Cristian Floo", datetime.date.today()), ("Gato miau miau", datetime.date.today())]
}}#nombre y disponibilidad

#clase para cada equipo (esta vaina no es para nada necesaria en el reto, pero la dejo aqui para preguntar mas tarde como implementarla)
class Equipo:
    def __init__(self, nombre, disponibilidad=True):
        self.nombre = nombre
        self.disponibilidad = disponibilidad

#Funciones

#fun existencias
def existencias():
    if not inventario_equipos:
        return False
    return True

#Fun mostrar_equipos
def mostrar_equipos():
    if not existencias():
        return print("No hay equipos disponibles")
    for clave, valor in inventario_equipos.items():
        print(f"Equipo: {clave}, estado: {'Disponible' if valor['disponibilidad']  else 'prestado'}")


#fun registrar prestamo
def registrar_prestamo(nombre_equipo):
    if nombre_equipo not in inventario_equipos:
        print("El equipo no existe")
        return
    if not inventario_equipos[nombre_equipo]['disponibilidad']:
        print("El equipo no esta disponible")
        return
    while True:
        input_usuario = input("Ingrese su nombre")
        if input_usuario == "" or input_usuario.isspace():
            print("El nombre no puede estar vacio")
        else:
            inventario_equipos[nombre_equipo]['disponibilidad'] = False
            inventario_equipos[nombre_equipo]['prestamos'].append((input_usuario, datetime.date.today()))
            print(f"Equipo {nombre_equipo} prestado a {input_usuario} el dia {datetime.date.today()}")
            return 

#fun devolver equipo
def devolver_equipo(nombre_equipo):
    if nombre_equipo not in inventario_equipos:
        return print("El equipo no existe")
    if inventario_equipos[nombre_equipo]['disponibilidad']:
        return print("El equipo ya no ha sido prestado")
    
    inventario_equipos[nombre_equipo]['disponibilidad'] = True
    print(f"Equipo {nombre_equipo} ha sido devuelto")
    return 

#fun ver hisotorial
def ver_historial():
    for clave, valor in inventario_equipos.items():
        print(f"Equipo: {clave}")
        if not valor['prestamos']:
            print("Sin prestamos aun")
        for prestamo in valor['prestamos']:
            print(f"Prestado a: {prestamo[0]} el dia {prestamo[1]}")
    
# agregar equipo
def agregar_equipo(nombre_equipo):
    if nombre_equipo == "" or nombre_equipo.isspace():
        return print("El nombre del equipo no puede estar vacio")
    if nombre_equipo in inventario_equipos:
        return print("El equipo ya existe")
    inventario_equipos[nombre_equipo] = {'disponibilidad': True, 'prestamos': []}
    print(f"Equipo {nombre_equipo} ha sido creado y agregado al inventario")
    return 
#Menu
def main():

    
    
    #variables
    bucle = True
    opcion = 0
    input_usuario = ""
    while bucle:
        print("Bienvendido a SPE - Sistema de Préstamos de Equipos")
        print("1. Ver todos los equipos")
        print("2. Prestar un equipo")
        print("3. Devolver un equipo")
        print("4. Ver el historial de prestamos")
        print("5. Agregar nuevo equipo")   
        print("6. salir")
        print("Seleccione una opcion del 1-6")
        try:
            opcion = int(input())
        except ValueError:
            print("Ingrese un número válido")
            continue
        match opcion:
            case 1: 
                print("Lista de equipos en inventario:")
                mostrar_equipos()
            case 2:
                print("Prestar un equipo")
                print("Ingrese el nombre del equipo a prestar:")
                input_usuario = input()
                registrar_prestamo(input_usuario)
            case 3:
                print("Devolver un equipo")
                input_usuario = input("Ingrese el nombre del equipo a devolver:")
                devolver_equipo(input_usuario)
            case 4:
                print("Ver historial de prestamos")
                ver_historial()
            case 5:
                print("Agregar un nuevo equipo")
                agregar_equipo(input("Ingrese el nombre del nuevo equipo:"))
            case 6:
                print("Ha salido del sistema")
                bucle = False
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()