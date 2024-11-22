import math
import random

class Raices:
    def __init__(self):

        self.a = random.randint(10000000, 99999999)  
        self.b = random.randint(10000000, 99999999)
        self.c = random.randint(10000000, 99999999)
        print(f"Coeficientes generados: a={self.a}, b={self.b}, c={self.c}")

    def obtenerRaices(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            print(f"Las dos raices son: {raiz1} y {raiz2}")
        else:
            print("No hay dos soluciones reales.")

    def obtenerRaiz(self):
        discriminante = self.getDiscriminante()
        if discriminante == 0:
            raiz = -self.b / (2 * self.a)
            print(f"La raiz unica es: {raiz}")
        else:
            print("No hay una raiz unica.")

    def getDiscriminante(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def tieneRaices(self):
        return self.getDiscriminante() >= 0

    def tieneRaiz(self):
        return self.getDiscriminante() == 0

    def calcular(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            print(f"Las soluciones son: {raiz1} y {raiz2}")
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            print(f"La solucion unica es: {raiz}")
        else:
            print("No existe solucion real.")
ecuacion = Raices()
ecuacion.calcular()
ecuacion.obtenerRaices()
ecuacion.obtenerRaiz()
print(f"Discriminante: {ecuacion.getDiscriminante()}")
print(f"Tiene dos raices: {ecuacion.tieneRaices()}")
print(f"Tiene una raz: {ecuacion.tieneRaiz()}")
