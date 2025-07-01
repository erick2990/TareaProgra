lista_Numeros = []
fin = True
Mayor =0

def buscar(lista):
    lista.sort()
    resultado = lista[-1] #El inidce sera negativo ya que apunta al ultimo elemento
    return resultado

while fin:
    entrada = int(input('Ingrese el numero y si desea cerrar ingrese 0:  '))

    if entrada>0:
        lista_Numeros.append(entrada)
    elif entrada<=0:
        print('Se finalizo el ingreso con exito...')
        fin = False

Mayor = buscar(lista_Numeros)
print(f'El numero mayor encontrado es: {Mayor}')