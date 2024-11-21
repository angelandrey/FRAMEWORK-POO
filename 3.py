class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_edad(self):
        return self.edad


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def retirar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.cantidad}")
        else:
            print("Saldo insuficiente.")

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Saldo: {self.cantidad}")


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        if 0 <= bonificacion <= 100:
            self.bonificacion = bonificacion
        else:
            print("La bonificación debe estar entre 0 y 100.")

    def esTitularValido(self):
        edad = self.titular.get_edad()
        return 18 <= edad < 25

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar esta operación. La cuenta debe tener entre 18 y 25 años.")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}%")


# Ejemplo de uso:
persona = Persona("Ana", 22, "987654321")
cuenta_joven = CuentaJoven(persona, 500.0, 2.5)

cuenta_joven.mostrar()
cuenta_joven.retirar(100)

cuenta_joven.set_bonificacion(5.0)
cuenta_joven.mostrar()

persona.edad = 26  # Cambiamos la edad de Ana
cuenta_joven.retirar(50)  # Ahora el retiro no se permitirá
