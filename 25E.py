Lista_Tareas = []


fin = True

while fin:
    opcion = 0
    opcion = int(input('Bienvenido ingrese una opcion: \r\n1.Agregar Tareas \r\n2.Marcar Tarea completada \r\n3.Ver lista \r\n4.Salir'))


    match opcion:
        case 1:
            asignacion = input('Ingrese cual es la tarea que debe hacer: ')
            Lista_Tareas.append(asignacion)
            print('Tarea asignada con exito')

        case 2:
            cont =1
            num_Tarea = 0
            for tmp in Lista_Tareas:
                print(f'{cont}. Pendiente {tmp} ')
                cont+=1

            num_Tarea = int(input('Ingrese el numero de tarea que ya logro completar: '))
            del Lista_Tareas[num_Tarea-1] #Se elimina lo que hay en esa ubicacion
            print('Finalizado con exito!!!')

        case 3:
            print('Lista actual de pendientes')
            for tmp in Lista_Tareas:
                print(f'Pendiente: {tmp}')

        case 4:
            print('ADIOS!!!')
            fin=False

        case _:
            print("Opcion invalida")