class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def deposito(self):
        monto = float(input('Ingrese la cantidad que desea depositar: '))
        self.saldo = self.saldo+monto
        print(f'Se deposito correctamente {monto} en la cuenta')

    def retirar(self):
        monto = float(input('Ingrese la cantidad a retirar debe ser menor a lo que posee en la cuenta'))
        if monto>self.saldo:
            print('Dinero insuficiente para realizar este proceso')
        elif monto>0 and monto<=self.saldo:
            print('Se realizo el retiro con exito!!!!')
            self.saldo = self.saldo-monto

    def total(self):
        print('Su estado de cuenta es el siguiente')
        print(f'Actualmente tiene {self.saldo}')


cuenta1 = CuentaBancaria(2000)
cuenta1.total()
cuenta1.deposito()
cuenta1.deposito()
cuenta1.total()
cuenta1.deposito()
cuenta1.total()
cuenta1.retirar()
cuenta1.retirar()
cuenta1.total()