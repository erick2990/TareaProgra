Estudiantes = []

class Estudiante:

    def __init__(self, nombre, nota, promedio):
        self.nombre = nombre
        self.nota = nota
        self.promedio = promedio


    def asignar_Nota(self):
        cursos =0
        nota =0
        sumatoria =0
        cursos = int(input('Ingrese cuantos cursos lleva el estudiante'))
        for x in range(1, cursos+1, 1):
            nota = int(input(f'Ingrese la nota del {x} curso: '))
            sumatoria = sumatoria + nota
        self.promedio = sumatoria / cursos

    def mostrarPromedio(self):
        print(f'Nombre: {self.nombre} Mi promedio actualmente es de: {self.promedio}')

fin = True

while fin:
    entrada = int(input('1. Registrar Estudiante \r\n2. Ingresar notas \r\n3. Consultar promedios'))
    match entrada:
        case 1:
            nombreTmp = input('ingrese el nombre del estudiante: ')
            tmp = Estudiante(nombreTmp, 0,0)
            Estudiantes.append(tmp)
            print('Estudiante registrado con exito!!!')
        case 2:
            for t in Estudiantes:
                t.asignar_Nota()

        case 3:
            print('Se mostrara los promedios actuales')
            for m in Estudiantes:
                m.mostrarPromedio()
        case _:
            print('No existe esta opcion')