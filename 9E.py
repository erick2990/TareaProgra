
paso_Inicial =1000
hora = 1
fin = True

while fin:
    print(f'En {hora} hora dio {paso_Inicial} pasos...')

    if paso_Inicial==10000:
        print(f'Felicidades llego a los 10,000 pasos en {hora} horas ')
        fin = False
    paso_Inicial += 1000
    hora += 1