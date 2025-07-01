def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


ingreso = int(input("Ingresa un número: "))
if primo(ingreso):
    print(f"{ingreso} es un número primo.")
else:
    print(f"{ingreso} no es primo.")