class Empleado:
    PLUS = 300  

    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getSalario(self):
        return self.salario

    def setSalario(self, salario):
        self.salario = salario

    def plus(self):
        pass 

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}$"
    
class Comercial(Empleado):
    def __init__(self, nombre, edad, salario, comision):
        super().__init__(nombre, edad, salario)
        self.comision = comision

    def getComision(self):
        return self.comision

    def setComision(self, comision):
        self.comision = comision

    def plus(self):
        if self.edad > 30 and self.comision > 200:
            self.salario += self.PLUS
            print(f"Se ha aplicado el PLUS al empleado Comercial {self.nombre}. Nuevo salario: {self.salario}$")

    def __str__(self):
        return super().__str__() + f", Comision: {self.comision}$"


class Repartidor(Empleado):
    def __init__(self, nombre, edad, salario, zona):
        super().__init__(nombre, edad, salario)
        self.zona = zona

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona

    def plus(self):
        if self.edad < 25 and self.zona == "zona 3":
            self.salario += self.PLUS
            print(f"Se ha aplicado el PLUS al empleado Repartidor {self.nombre}. Nuevo salario: {self.salario}$")

    def __str__(self):
        return super().__str__() + f", Zona: {self.zona}"
if __name__ == "__main__":

    empleado_comercial = Comercial("jhonnny Meneeses", 35, 1500, 250)
    empleado_repartidor = Repartidor("Dora Veizaga", 24, 1200, "zona 3")
    
 
    print(empleado_comercial)
    print(empleado_repartidor)
    

    empleado_comercial.plus()  
    empleado_repartidor.plus() 
    
  
    print(empleado_comercial)
    print(empleado_repartidor)
