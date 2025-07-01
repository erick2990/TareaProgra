from itertools import product


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def descuento(self):
        print('Aplicando descuentos')
        if self.stock>20 and self.precio>100: #se aplica si el producto cuesta mas de 100
            self.precio = self.precio - (self.precio * 0.10) #Se aplica un 10% si hay mucho stock del producto


    def Mostrar(self):
        print(f'Producto: {self.nombre}  precio: {self.precio}  stock: {self.stock}')



producto1 = Producto("Aceite", 20, 100)
producto1.Mostrar() #muestra sin descuento
producto1.descuento() #aplica descuento
producto1.Mostrar() # muestra con descuento

producto2 = Producto("Computador", 1000, 40)
producto2.Mostrar()
producto2.descuento()
producto2.Mostrar()



