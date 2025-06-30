
nombres = []
Agregar = True
cont = 0

while Agregar:
    ingreso = input(f'Ingrese {cont+1} nombre cualquiera si tiene una vocal mucho mejor: ')
    nombres.append(ingreso) # se guarda lo que se ingreso
    cont+=1 #aumenta despues de que finalice un ciclo y luego
    if cont ==10:
        Agregar = False



nombre_vocal = list(filter(lambda nombre: nombre[0].lower() in "aeiou", nombres))
print(nombre_vocal)
