from netaddr.strategy.ipv6 import packed_to_int


def gc():
    fa = float(input('Igrese los grados en Fahrenheit: '))
    celsius = (fa-32)/1.8
    print(f'Temperatura en celsius {celsius} ')
def gf():
    ce = float(input('Ingrese los grados en Celsius: '))
    fah = (ce*1.8)+32
    print(f'Temperatura en Fahrenheit {fah} ')

temperatura = {
    1: gc,
    2: gf
}

fin=True

while fin:
    print('\r\t\tCONVERTIDOR:')
    entrada = int(input('1.Fahrenheit a Celsius\r\n 2.Celsius a Fahrenheit \r\n3. Salir\r\n'))
    if entrada ==3:
        print('Adios')
        fin=False

    temperatura.get(entrada, lambda:"Opcion no valida")()