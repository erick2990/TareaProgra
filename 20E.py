class Estudiante:

    def __init__(self, curso1, curso2, curso3):
        self.curso1 = curso1
        self.curso2 = curso2
        self.curso3 = curso3

    def promedio(self):
        res = (self.curso1 + self.curso2 + self.curso3) /3
        return res

nota1 =0
nota2 =0
nota3 =0

nota1 = int(input('Ingrese la nota del primer curso: '))
nota2 = int(input('Ingrese la nota del segundo curso: '))
nota3 = int(input('Ingrese la nota del tercer curso: '))
print('Se calculara el promedio...')

estudiante = Estudiante(nota1, nota2, nota3)
print(f'El promedio del estudiante es: {estudiante.promedio()}')