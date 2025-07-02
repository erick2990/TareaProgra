lista = [] #lista vacia


fin = True

while fin:
    ingreso =0 #Se inicializa vacia por si presiona algo erroneo
    ingreso =int(input('1.Agregar elementos \r\n2.Buscar \r\n3.Elimina \r\n4.Mostrar Todo \r\n5.Salir'))
    match ingreso:
        case 1:
            cadena = input('Ingresa lo que deseas añadir a la lista:  ')
            lista.append(cadena)
            print('Listoo!!!!1')
        case 2:
            buscar = input('Ingresa lo que estas buscando dentro de la lista: ')
            for x in lista:
                if x==buscar:
                    print('Si se encontro lo que estabas buscando')
                else:
                    print('No existe este elemento')
        case 3:
            eliminar = input('Ingresa que es lo que deseas eliminar: ')
            lista.remove(eliminar)
            print('Se elimino con exito')

        case 4:
            print('Imprimiendo todo:  ')
            for m in lista:
                print(f'{m}')
        case 5:
            print('Finalizo con exito!!!')
            fin = False
        case _:
            print('Pulsaste un boton incorrecto')