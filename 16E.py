class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor_Edad(self):
        if self.edad >=18:
            print(f'Eres una persona mayor de edad, tienes {self.edad} anios')
        elif self.edad>0 and self.edad <18:
            print(f'Eres muy joven aún, tienes {self.edad} anios')


persona1 = Persona("Erick", 21)
persona2 = Persona("Alexander", 15)

persona1.mayor_Edad()
persona2.mayor_Edad()