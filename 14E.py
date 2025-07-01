
def vocal(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    numero_Vocales =0

    for ev in palabra:
        if ev in vocales: #Recorre cada parte de la cadena y la compara con la cadena que contiene cualquier tipo o aso de vocal
            numero_Vocales += 1 #Aumenta si existen vocales
    return numero_Vocales

entrada = input('Escriba una palabra:  ')
print(f'Existen {vocal(entrada)} vocales en la palabra {entrada}')