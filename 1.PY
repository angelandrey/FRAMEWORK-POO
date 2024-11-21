class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getter y setter para el nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("El nombre debe ser una cadena no vacía.")
    
    # Getter y setter para la edad
    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número entero positivo.")
    
    # Getter y setter para el DNI
    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:  # Suposición: el DNI tiene 9 caracteres
            self.dni = dni
        else:
            print("El DNI debe ser una cadena de 9 caracteres.")
    
    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    
    # Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18


# Ejemplo de uso
persona = Persona()
persona.set_nombre("Juan")
persona.set_edad(20)
persona.set_dni("123456789")
persona.mostrar()

if persona.es_mayor_de_edad():
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")
