import random

class Persona:
    HOMBRE = 'H'
    MUJER = 'M'
    PESO_BAJO = -1
    PESO_IDEAL = 0
    SOBREPESO = 1
    SEXO_INCORRECTO = 'H'

    def __init__(self, nombre="", edad=0, ci="", sexo=HOMBRE, peso=0.0, altura=0.0):
        self._nombre = nombre
        self._edad = edad
        self._ci = ci if ci else self.generaCI()
        self._sexo = self.comprobarSexo(sexo)
        self._peso = peso
        self._altura = altura

    def calcularIMC(self):
        if self._altura > 0:
            imc = self._peso / (self._altura ** 2)
            if imc < 20:
                return self.PESO_BAJO
            elif 20 <= imc <= 25:
                return self.PESO_IDEAL
            else:
                return self.SOBREPESO
        return None

    def esMayorDeEdad(self):
        return self._edad >= 18

    def comprobarSexo(self, sexo):
        if sexo not in [self.HOMBRE, self.MUJER]:
            return self.HOMBRE
        return sexo

    def generaCI(self):
        numero_ci = random.randint(10000000, 99999999)
        letra_ci = chr(random.randint(65, 90))  # Letra aleatoria mayúscula
        return f"{numero_ci}{letra_ci}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def ci(self):
        return self._ci

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        self._sexo = self.comprobarSexo(valor)

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor
def crear_persona_por_teclado():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (H para hombre, M para mujer): ").upper()
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese la altura (m): "))
    return Persona(nombre, edad, sexo=sexo, peso=peso, altura=altura)

def crear_persona_sin_peso_altura():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (H para hombre, M para mujer): ").upper()
    return Persona(nombre, edad, sexo=sexo)

def mostrar_informacion_persona(persona):
    print(f"\nInformación de {persona.nombre}:")
    print(f"Edad: {persona.edad}")
    print(f"Sexo: {persona.sexo}")
    print(f"CI: {persona.ci}")
    print(f"Peso: {persona.peso} kg")
    print(f"Altura: {persona.altura} m")
    print(f"Mayor de edad: {'Si' if persona.esMayorDeEdad() else 'No'}")

def mensaje_imc(persona):
    imc = persona.calcularIMC()
    if imc == Persona.PESO_BAJO:
        print("Esta por debajo de su peso ideal.")
    elif imc == Persona.PESO_IDEAL:
        print("Esta en su peso ideal.")
    elif imc == Persona.SOBREPESO:
        print("Tiene sobrepeso.")
    else:
        print("No se puede calcular el IMC debido a datos insuficientes.")

def ejecutar():
    print("Creacion del primer objeto:")
    persona1 = crear_persona_por_teclado()
    
    print("\nCreacion del segundo objeto:")
    persona2 = crear_persona_sin_peso_altura()
    
    print("\nCreacion del tercer objeto (por defecto):")
    persona3 = Persona() 
    persona3.nombre = "Choquito"
    persona3.edad = 25
    persona3.sexo = "H"
    persona3.peso = 70
    persona3.altura = 1.75
    
    for persona in [persona1, persona2, persona3]:
        mostrar_informacion_persona(persona)
        mensaje_imc(persona)

ejecutar()