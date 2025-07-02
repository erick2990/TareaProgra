#Se utilizara diccionario
import math
from os import MFD_ALLOW_SEALING

def a_Circulo():
    radio = int(input('Ingrese el radio de la circunferencia: '))
    res = math.pi*(radio**2)
    print(f'El área de la circunferencia es: {res}')

def a_Cuadrado():
    lado = int(input('Ingrese la longitud de un lado del cuadrado: '))
    res = lado**2
    print(f'El área del cuadrado es: {res}')

def a_Triangulo():
    base = int(input('Ingrese la medida de la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))
    res = (base*altura)/2
    print(f'El area del triangulo es: {res}')


Areas = {
    1: a_Circulo,
    2: a_Cuadrado,
    3: a_Triangulo
}

fin=True

while fin:
    print('Calculo de áreas: \r\n1. Circulo \r\n2.Cuadrado \r\n3.Triangulo \r\n4.Salir')
    opcion = int(input())
    if opcion==4:
        fin=False

    Areas.get(opcion, lambda:"Opcion no valida")()
    #Sirve para obtener los items de Areas y lambda es el caso que no exista el item en el diccionario el segundo parentesis
    #Sirve para ejecutar las funciones
