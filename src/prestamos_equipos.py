import datetime 

# listas para almacenar de forma ordenada el historial de datos de cada equipo
# tuplas para los datos de cada préstamo (usuario, fecha)
# Diccionarios para almacenar todos los equipos, su estado, disponibilidad y prestamos asociados
#Funciones modulares 
#Menu interactivo 

#Clases

class Inventario:
    def __init__(self):
        self.equipos = {}

    def agregar(self, nombre):
        if not nombre or nombre.isspace():
            print("El nombre del equipo no puede estar vacio")
            return False
        if nombre in self.equipos:
            print("El equipo ya existe")
            return False
        self.equipos[nombre] = Equipo(nombre)
        print(f"Equipo {nombre} ha sido creado y agregado al inventario")
        return True

    def obtener(self, nombre):
        return self.equipos.get(nombre)

    def existe(self, nombre):
        return nombre in self.equipos

    def mostrar_todos(self):
        if not self.equipos:
            print("No hay equipos disponibles")
            return
        for equipo in self.equipos.values():
            equipo.mostrar()

    def mostrar_historial(self):
        for equipo in self.equipos.values():
            equipo.mostrar_historial()

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True
        self.prestamos = []

    def prestar(self, usuario):
        if not self.disponible:
            return False
        self.disponible = False
        self.prestamos.append(Prestamo(usuario, datetime.date.today()))
        return True

    def devolver(self):
        if self.disponible:
            return False
        self.disponible = True
        return True

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Equipo: {self.nombre}, estado: {estado}")

    def mostrar_historial(self):
        print(f"Equipo: {self.nombre}")
        if not self.prestamos:
            print("  Sin prestamos aun")
        for p in self.prestamos:
            print(f"  {p}")


class Prestamo:
    def __init__(self, usuario, fecha):
        self.usuario = usuario
        self.fecha = fecha

    def __str__(self):
        return f"Prestado a: {self.usuario} el dia {self.fecha}"





#Menu
def main():
    inventario = Inventario()
   
    pc_gamer = Equipo("PC gamer")
    pc_gamer.prestamos.append(Prestamo("Cristian Floo", datetime.date.today()))
    pc_gamer.prestamos.append(Prestamo("Gato miau miau", datetime.date.today()))
    pc_gamer.disponible = False
    inventario.equipos["PC gamer"] = pc_gamer

    while True:
        print("Bienvendido a SPE - Sistema de Prestamos de Equipos")
        print("1. Ver todos los equipos")
        print("2. Prestar un equipo")
        print("3. Devolver un equipo")
        print("4. Ver el historial de prestamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero valido")
            continue

        match opcion:
            case 1:
                print("Lista de equipos en inventario:")
                inventario.mostrar_todos()
            case 2:
                nombre = input("Ingrese el nombre del equipo a prestar: ")
                equipo = inventario.obtener(nombre)
                if not equipo:
                    print("El equipo no existe")
                    continue
                usuario = input("Ingrese su nombre: ")
                if not equipo.prestar(usuario):
                    print("El equipo no esta disponible")
                else:
                    print(f"Equipo {nombre} prestado a {usuario}")
            case 3:
                nombre = input("Ingrese el nombre del equipo a devolver: ")
                equipo = inventario.obtener(nombre)
                if not equipo:
                    print("El equipo no existe")
                elif not equipo.devolver():
                    print("El equipo no estaba prestado")
                else:
                    print(f"Equipo {nombre} ha sido devuelto")
            case 4:
                print("Historial de prestamos:")
                inventario.mostrar_historial()
            case 5:
                inventario.agregar(input("Ingrese el nombre del nuevo equipo: "))
            case 6:
                print("Ha salido del sistema")
                break
            case _:
                print("Opcion no valida")

if __name__ == "__main__":
    main()