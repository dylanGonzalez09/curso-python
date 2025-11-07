# Cuenta bancaria
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito exitoso: {cantidad}. Nuevo balance: {self.balance}")
        else:
            print("Cantidad de depósito inválida.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro exitoso: {cantidad}. Nuevo balance: {self.balance}")
        else:
            print("Cantidad de retiro inválida o fondos insuficientes.")

def creaer_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    return Cliente(nombre, apellido, numero_cuenta)

def inicio():
    cliente = creaer_cliente()
    while True:
        print("\nOpciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == '3':
            print("Gracias por usar el sistema bancario.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

inicio()