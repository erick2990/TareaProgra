
n=0

numero = input('Ingrese un numero N para realizar una piramide de *')

n = int(numero)

if n>0:
    for x in range(1, n+1):
        espacio = " "* (n-x)   #Espacios necesarios para centrar
        fig = "*" * (2*x-1)    #Dibuja el triangulo con asterisco
        print(espacio + fig)
