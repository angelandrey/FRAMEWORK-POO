class Cuenta:
    # Constructor de la clase Cuenta
    # El titular es obligatorio y debe ser una instancia de la clase Persona.
    # La cantidad es opcional, por defecto será 0.0 si no se especifica.
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular  # Asignamos el titular de la cuenta (persona).
        self.cantidad = cantidad  # Asignamos el saldo de la cuenta, por defecto 0.0.

    # Getter para obtener el titular de la cuenta
    def get_titular(self):
        return self.titular  # Retorna el titular de la cuenta.

    # Setter para modificar el titular de la cuenta
    def set_titular(self, titular):
        if isinstance(titular, Persona):  # Validamos que el titular sea una instancia de la clase Persona.
            self.titular = titular  # Asignamos el nuevo titular.
        else:
            print("El titular debe ser una instancia de la clase Persona.")  # Mensaje de error si no es una Persona.

    # Getter para obtener el saldo de la cuenta
    def get_cantidad(self):
        return self.cantidad  # Retorna el saldo actual de la cuenta.

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")  # Muestra el nombre del titular usando el método get_nombre de Persona.
        print(f"Cantidad: {self.cantidad:.2f}")  # Muestra el saldo de la cuenta con 2 decimales.

    # Método para ingresar dinero a la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:  # Validamos que la cantidad a ingresar sea positiva.
            self.cantidad += cantidad  # Aumentamos el saldo de la cuenta.
        else:
            print("La cantidad a ingresar debe ser positiva.")  # Mensaje de error si la cantidad es negativa o cero.

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:  # Validamos que la cantidad a retirar sea positiva.
            self.cantidad -= cantidad  # Disminuimos el saldo de la cuenta.
        else:
            print("La cantidad a retirar debe ser positiva.")  # Mensaje de error si la cantidad es negativa o cero.

# Clase Persona para el ejemplo de uso
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre  # Inicializa el nombre de la persona.
        self.edad = edad  # Inicializa la edad de la persona.
        self.dni = dni  # Inicializa el DNI de la persona.

    # Getter para obtener el nombre
    def get_nombre(self):
        return self.nombre  # Retorna el nombre de la persona.

# Ejemplo de uso de las clases Persona y Cuenta
persona = Persona("Juan", 30, "123456789")  # Creamos una persona llamada Juan.
cuenta = Cuenta(persona, 1000.50)  # Creamos una cuenta con un saldo inicial de 1000.50 y con Juan como titular.

# Mostrar los datos de la cuenta
cuenta.mostrar()

# Ingresar dinero en la cuenta
cuenta.ingresar(200)  # Ingresamos 200 en la cuenta.
cuenta.mostrar()  # Mostramos los datos de la cuenta después del ingreso.

# Retirar dinero de la cuenta
cuenta.retirar(500)  # Retiramos 500 de la cuenta.
cuenta.mostrar()  # Mostramos los datos de la cuenta después del retiro.

# Intentar ingresar una cantidad negativa (no debería hacer nada)
cuenta.ingresar(-100)  # Intentamos ingresar -100, lo cual no debería ser permitido.
cuenta.mostrar()  # Mostramos los datos para verificar que el saldo no cambió.

# Intentar retirar una cantidad negativa (no debería hacer nada)
cuenta.retirar(-50)  # Intentamos retirar -50, lo cual no debería ser permitido.
cuenta.mostrar()  # Mostramos los datos para verificar que el saldo no cambió.
