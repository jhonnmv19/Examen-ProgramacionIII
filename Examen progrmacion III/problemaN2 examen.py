class Cuenta:
    def __init__(self, titular, cantidad=0):
       
        self.titular = titular
        self.cantidad = cantidad

   
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

  
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad debe ser positiva para ingresar.")

  
    def retirar(self, cantidad):
        if cantidad < 0:
            print("La cantidad debe ser positiva para retirar.")
        else:
            self.cantidad = max(0, self.cantidad - cantidad)


titular = input("Ingrese el titular de la cuenta: ")
cantidad_inicial = float(input("Ingrese la cantidad inicial (puede ser 0): "))


cuenta1 = Cuenta(titular, cantidad_inicial)


print(f"Titular: {cuenta1.get_titular()}")
print(f"Cantidad: {cuenta1.get_cantidad()}")


cuenta1.ingresar(500)  
print(f"Cantidad después de ingresar: {cuenta1.get_cantidad()}")

cuenta1.retirar(2000)  
print(f"Cantidad después de intentar retirar 2000: {cuenta1.get_cantidad()}")

cuenta1.retirar(300)  
print(f"Cantidad después de retirar 300: {cuenta1.get_cantidad()}")
