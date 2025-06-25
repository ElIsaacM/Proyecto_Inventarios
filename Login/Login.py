import login.Encriptacion as enc
from roles.Clientes import Menu_cliente
from roles.Empleados import Menu_empleado
from roles.Admin import Menu_admin

def validar_acceso(usuario_ingresado, contrasena_ingresada):
    with open('Datos/usuarios.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            partes = linea.strip().split(',')

            if len(partes) < 3:
                continue

            usuario = partes[0]
            contrasena_encriptada = partes[1]
            clave = partes[2]
            rol = partes[3] if len(partes) > 3 else 'cliente'

            if usuario == usuario_ingresado:
                # Usar la clave almacenada para encriptar la contraseña ingresada
                contrasena_encriptada_ingresada = enc.Encriptar(contrasena_ingresada, clave)
                if contrasena_encriptada_ingresada == contrasena_encriptada:
                    print('Acceso concedido')
                    return True, rol
                else:
                    print('Contraseña incorrecta')
                    return False, None
        print('Usuario no encontrado')
        return False, None
    
def Validar_rol():
    usuario = input('Usuario: ')
    contrasena = input('Contrasena: ')
    validar,rol = validar_acceso(usuario, contrasena) 

    if validar:
        print(f'\nBienvenido: {usuario}, (Rol: {rol})')
        if rol in ('admin', 'root'):
            Menu_admin(rol)
        elif rol == 'empleado':
            Menu_empleado(rol)
        elif rol == 'cliente':
            Menu_cliente(rol)
        else:
            print('Rol desconocido.')
    else:
        print('Acceso denegado')