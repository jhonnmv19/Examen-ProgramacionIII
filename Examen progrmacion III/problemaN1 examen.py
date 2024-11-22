class Bebida:
    def __init__(self, identificador, litros, precio, marca):
        self.identificador = identificador
        self.litros = litros
        self.precio = precio
        self.marca = marca

    def mostrar_informacion(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases")


class AguaMineral(Bebida):
    def __init__(self, identificador, litros, precio, marca, manantial):
        super().__init__(identificador, litros, precio, marca)
        self.manantial = manantial

    def mostrar_informacion(self):
        return (f"Agua Mineral - ID: {self.identificador}, Litros: {self.litros}, Precio: {self.precio}, "
                f"Marca: {self.marca}, Manantial: {self.manantial}")


class BebidaAzucarada(Bebida):
    def __init__(self, identificador, litros, precio, marca, porcentaje_azucar):
        super().__init__(identificador, litros, precio, marca)
        self.porcentaje_azucar = porcentaje_azucar

    def mostrar_informacion(self):
        return (f"Bebida Azucarada - ID: {self.identificador}, Litros: {self.litros}, Precio: {self.precio}, "
                f"Marca: {self.marca}, Azucar: {self.porcentaje_azucar}%")
class Almacen:
    def __init__(self):
        self.bebidas = []

    def agregar_producto(self, bebida):
        if bebida:
            self.bebidas.append(bebida)
            print("Producto agregado correctamente.")
        else:
            print("Error: Producto invalido.")

    def calcular_precio_total(self):
        return sum(bebida.precio for bebida in self.bebidas)

    def calcular_precio_por_marca(self, marca):
        return sum(bebida.precio for bebida in self.bebidas if bebida.marca.lower() == marca.lower())

    def mostrar_informacion(self):
        if not self.bebidas:
            print("No hay productos en el almacen.")
        else:
            for bebida in self.bebidas:
                print(bebida.mostrar_informacion())
def main():
    almacen = Almacen()
    cantidad_productos = int(input("¿Cuantos productos deseas agregar? "))

    for _ in range(cantidad_productos):
        print("\n¿Es Agua Mineral (1) o Bebida Azucarada (2)?")
        tipo = int(input("Selecciona una opcion: "))

        identificador = input("Identificador: ")
        litros = float(input("Litros: "))
        precio = float(input("Precio: "))
        marca = input("Marca: ")

        if tipo == 1:
            manantial = input("Nombre del Manantial: ")
            bebida = AguaMineral(identificador, litros, precio, marca, manantial)
        elif tipo == 2:
            porcentaje_azucar = float(input("Porcentaje de Azucar: "))
            bebida = BebidaAzucarada(identificador, litros, precio, marca, porcentaje_azucar)
        else:
            print("Opcion no valida. Producto no agregado.")
            continue

        almacen.agregar_producto(bebida)

    print("\n--- Informacion de las Bebidas ---")
    almacen.mostrar_informacion()

    print("\nPrecio total de todas las bebidas: {:.2f}".format(almacen.calcular_precio_total()))

    marca_busqueda = input("\nIngresa la marca para calcular el precio total: ")
    print("Precio total de la marca {}: {:.2f}".format(
        marca_busqueda, almacen.calcular_precio_por_marca(marca_busqueda)))


if __name__ == "__main__":
    main()
