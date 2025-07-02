
class Usuarios:

    def __init__(self, us, ps):
           self.us = us
           self.ps = ps



Admin = Usuarios("Admin", "Admin123")
Invitado = Usuarios("Invitado", "12345")


name = input('Ingrese su user name: ')
contra = input('Ingrese su contraseña: ')
if name == Admin.us and contra == Admin.ps:
    print('Bienvenido Administrador...')
elif name == Invitado.us and contra == Invitado.ps:
    print('Bienvenido invitado...')
