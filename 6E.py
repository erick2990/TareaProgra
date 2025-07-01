
class Admin:
    def __init__(self, us, passw):
         self.us = us
         self.passw = passw


persona = Admin("admin", "admin123")
correcto = True

while correcto:
    user = input('Ingrese su usuario: ')
    contra = input('Ingrese su contraseña: ')
    if user==persona.us and contra==persona.passw:
        print('Accedio con exito')
        correcto=False

    else:
        print('Datos incorrectos vuelva a intentarlo')

