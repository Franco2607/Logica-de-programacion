class Persona:
    # Init = crear
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 17

    # imprimir
    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | apellido: {self.apellido} | edad: {self.edad}")

# Uso de la clase (Instanciación)
mi_juego = Persona("Andres", "Franco", 17)
mi_juego.mostrar_info()

# EXTRA

# LIFO

class inventario:

    def __init__(self):
        self.inventario = []
    
    def agregar1 (self, item1):
        self.inventario.append(item1)
    
    def eliminar1 (self):
        if self.count() == 0:
            return None
        return self.inventario.pop(0)
    
    def cantidad1 (self):
        return len(self.count)

    def print1 (self):
        for item in reversed(self.inventario):
            print(item)

my_inventario = inventario ()
my_inventario.push ("A")
my_inventario.push ("B")
my_inventario.push ("C")
print(my_inventario.count())
my_inventario.print()
my_inventario.pop()
print(my_inventario.count())

# FIFO

class fila():
    def __init__(self):
        self.fila = []
    
    def agregar (self, item):
        self.fila.append(item)
    
    def eliminar (self):
        if self.count() == 0:
            return None
        return self.fila.pop(0)
    
    def cantidad (self):
        return len(self.count)

    def print (self):
        for item in (self.fila):
            print(item)

my_fila = fila ()
my_fila.fila ("A")
my_fila.fila ("B")
my_fila.fila ("C")
print(my_fila.count())