class Perro:
    def __init__(self, nombre, edad, raza):
        # Inicializa los atributos nombre, edad y raza del perro
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def mostrar_informacion(self):
        # Método para imprimir la información del perro
        print("La información del perro es:")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad, "años")
        print("Raza:", self.raza)

# Creamos una instancia de la clase Perro
perro_husky = Perro("Hush", 25, "Husky Siberiano")

# Llamamos al método mostrar_informacion para mostrar la información del perro
perro_husky.mostrar_informacion()
