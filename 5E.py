import random

numeros_Aleatorios = []

contador = 0
generar = True

while generar:
    aleatorio = random.randint(1,100) #se instancia un numero random
    numeros_Aleatorios.append(aleatorio) #se añade un numero random a la lista
    contador +=1
    if contador ==20:
        generar =False


for x in numeros_Aleatorios:
    if x%3==0:
        print(f'Multiplo de 3:  {x}')