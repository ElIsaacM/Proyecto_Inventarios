import Encriptacion as enc

def validar_acceso(usuario_ingresado, contrasena_ingresada):
    with open('Datos/usuarios.txt', 'r', encoding='utf-8') as f:
        for linea in f:
            usuario, contrasena_encriptada, clave = linea.strip().split(',')
            if usuario == usuario_ingresado:
                # Usar la clave almacenada para encriptar la contraseña ingresada
                contrasena_encriptada_ingresada = enc.Encriptar(contrasena_ingresada, clave)
                if contrasena_encriptada_ingresada == contrasena_encriptada:
                    print('Acceso concedido')
                    return True
                else:
                    print('Contraseña incorrecta')
                    return False
        print('Usuario no encontrado')
        return False

# Ejemplo de uso:
usuario = input('Usuario: ')
contrasena = input('Contraseña: ')
if validar_acceso(usuario, contrasena):
    print('Bienvenido a la interfaz')
else:
    print('Acceso denegado')