import random

numero_Adivinar = random.randint(1,100) #se instancia un objeto random y se llama el constructor randint
fin = True
print(f'Se genero un numero random con exito!!!!! Adivinalo.....{numero_Adivinar}')

while fin:
    respuesta = int(input('Ingresa el numero que crees que es: '))
    if respuesta<numero_Adivinar:
        print('El numero es mayor que la cantidad que ingresaste, sigue intentando...')
    elif respuesta>numero_Adivinar:
        print('El numero es menor que la cantidad que ingresaste, sigue intentando...')
    elif respuesta == numero_Adivinar:
        print('Adivinaste con exito!!! Felicidades')
        fin=False #se finaliza el ciclo con exito