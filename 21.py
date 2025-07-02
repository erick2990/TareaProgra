#Se utilizara diccionario
import math
from os import MFD_ALLOW_SEALING

def a_Circulo():
    radio = int(input('Ingrese el radio de la circunferencia: '))
    res = math.pi*(radio**2)
    print(f'El área de la circunferencia es: {res} m^2')

def a_Cuadrado():
    lado = int(input('Ingrese la longitud de un lado del cuadrado: '))
    res = lado**2
    print(f'El área del cuadrado es: {res} m^2')

def a_Triangulo():
    base = int(input('Ingrese la medida de la base del triangulo: '))
    altura = int(input('Ingrese la altura del triangulo: '))
    res = (base*altura)/2
    print(f'El area del triangulo es: {res} m^2')


Areas = {
    1: a_Circulo,
    2: a_Cuadrado,
    3: a_Triangulo
}

def gc():
    fa = float(input('Igrese los grados en Fahrenheit: '))
    celsius = (fa-32)/1.8
    print(f'Temperatura en celsius {celsius}  C')
def gf():
    ce = float(input('Ingrese los grados en Celsius: '))
    fah = (ce*1.8)+32
    print(f'Temperatura en Fahrenheit {fah} Fa')

temperatura = {
    1: gc,
    2: gf
}


def calcular_Area():
    fin = True

    while fin:
        print('Calculo de áreas: \r\n1. Circulo \r\n2.Cuadrado \r\n3.Triangulo \r\n4.Salir')
        opcion = int(input())
        if opcion == 4:
            fin = False

        Areas.get(opcion, lambda: "Opcion no valida")()
        # Sirve para obtener los items de Areas y lambda es el caso que no exista el item en el diccionario el segundo parentesis
        # Sirve para ejecutar las funciones


def convertir_Temperatura():
    fin = True

    while fin:
        print('\r\t\tCONVERTIDOR:')
        entrada = int(input('1.Fahrenheit a Celsius\r\n 2.Celsius a Fahrenheit \r\n3. Salir\r\n'))
        if entrada == 3:
            print('Adios')
            fin = False

        temperatura.get(entrada, lambda: "Opcion no valida")()


menu = True

while menu:
    print('1.Calcular área \r\n2.Convertir una temperatura \t\n3.Salir programa')
    ingreso = 0
    ingreso = int(input())
    match ingreso:
        case 1:
            calcular_Area()
        case 2:
            convertir_Temperatura()
        case 3:
            print('Finalizo con exito')
            menu = False
        case _:
            print('Error dato inexistente')