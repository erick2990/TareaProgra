

numero_Positivos = []
promedio =0
res =0

fin =True

while fin:

    entrada = int(input('Ingrese una serie de numeros cuando desee finalizar solo ingrese uno negativo: '))
    if entrada >0:
        numero_Positivos.append(entrada) #Agrega todos los numeros que sean positivos

    elif entrada<0:
        print('Ingreso un numero negativo por tanto se finalizara el ciclo')
        fin = False #Finaliza entonces el ciclo


for positivo in numero_Positivos:
    res = res + positivo  #se suman todos los valores que lo conforma y luego ya se configura

promedio = res/len(numero_Positivos)   #la funcion len lo que hace es contar la longitud de la lista
print(f'Se ingresaron {len(numero_Positivos)} numeros positivos y el promedio es:  {promedio}')
