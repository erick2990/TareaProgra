numero = 0

entrada = int(input('Ingrese un umero entero para sumar todos los pares hastsa el mismo'))

if entrada <=0:
    print('Ingreso un valor erroneo intente nuevamente')
elif entrada>=1:
    res = 0

    for n in range(1, entrada+1):
        if n%2 == 0:
            res = res + n

    print(f'El resultado de la suma de todos los pares es: {res}')




