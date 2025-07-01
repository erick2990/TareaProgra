PIN = 1812
intentos = 1
Intento = True


while Intento:

    ingreso = int(input('Ingrese su PIN para acceder al cajero: '))

    if ingreso==PIN and intentos<=3:
        print('ACCEDIO CORRECTAMENTE AL CAJERO')
        Intento = False  #se cierra el ciclo pero accedio

    elif intentos>=3:
        print('Supero los 3 intentos se congelo su cuenta, llame a su banco')
        Intento = False # se cierra el ciclo pero se congelo su cuenta

    elif ingreso!=PIN:
        print(f'Le quedan {3-intentos}  intentos')
        intentos+=1 #se aumenta el contador si no esttuvo bien la contraseña
