import Encriptacion as enc

def Registro():
    usuario = input('Ingrese un nombre de usuario: ')
    try:
        with open('Datos/usuarios.txt', 'r') as f:
            for linea in f:
                usuario_existente = linea.strip().split(',')[0]
                if usuario == usuario_existente:
                    print('¡El usuario ya existe! Elija otro nombre.')
                    return
    except FileNotFoundError:
        pass  # El archivo no existe aún, se puede crear

    contrasena = input('Ingrese una contrasena: ')
    clave = input('ingrese una clave de recuperacion (4 caracteres): ')
    print('\n')
    if len(clave) == 4:
        print('clave valida')
        contrasena = enc.Encriptar(contrasena, clave)
        with open('Datos/usuarios.txt', 'a', encoding='utf-8') as f:
            f.write(f'{usuario},{contrasena},{clave}\n')
        print('Usuario agregado con exito!')
    else:
        print('la longitud de la clave debe ser de 4 caracteres!')

while True:
    print('\n----menu----')
    print('1. Registrarse')
    print('2. Salir')
    try:
        opcionReg = int(input('Que desea hacer: '))
        print('\n')
    except ValueError:
        print('Ingrese un numero valido')
        continue

    if opcionReg == 1:
        Registro()

    if opcionReg == 2:
        print('Gracias!')
        break