class Auto:

    def encender(self):
        print('\r\t\t\tEl carro esta encendido y avanzando')
    def apagar(self):
        print('\r\t\t\tEl carro esta apagado y paro')



fin=True
carro = Auto()

while fin:
     opcion = int(input('Presione \r\n1.Para encender el carro y avanzar \r\n2.Para apagar y pausar \r\n3.Salir'))

     match opcion:
         case 1:
             carro.encender()
         case 2:
             carro.apagar()
         case 3:
             print('\r\t\t\tSe finalizo el viaje')
             fin=False
         case _:
             print('Opcion inexistente')

