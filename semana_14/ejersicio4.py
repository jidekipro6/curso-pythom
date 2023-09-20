# Ejercicio 4: Encapsulamiento
# Crea una clase 'Banco' con un atributo 'saldo' que sea privado. 
# Agrega métodos para depositar, retirar y mostrar el saldo.


class Banco:

    def __init__(self):
        # Atributo privado para el saldo
        self._saldo = 0

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de ${cantidad} realizado.")
        else:
            print("El monto de depósito debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado.")
        else:
            print("Saldo insuficiente o monto de retiro no válido.")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self._saldo}")

# Ejemplo de uso
mi_banco = Banco()
mi_banco.mostrar_saldo()

mi_banco.depositar(1000)
mi_banco.mostrar_saldo()

mi_banco.retirar(500)
mi_banco.mostrar_saldo()
