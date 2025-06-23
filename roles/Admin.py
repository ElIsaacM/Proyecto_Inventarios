import Productos as prod

def Stock_bajo():
    for nombre, datos in prod.productos.items():
        if datos['stock'] <= 10:
            print(f'{nombre}: Stock = {datos['stock']}')

def Ver_usuarios():
    with open('Datos/usuarios.txt', 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 4:
                usuario, contrasena_encriptada, clave, rol = partes
                print(f"Usuario: {usuario}, Contraseña encriptada: {contrasena_encriptada}, Clave: {clave}, Rol: {rol}")
            else:
                usuario, contrasena_encriptada, clave = partes
                print(f"Usuario: {usuario}, Contraseña encriptada: {contrasena_encriptada}, Clave: {clave}, Rol: Cliente")

def Existe_usuario(usuario):
    with open('Datos/usuarios.txt', 'r') as f:
        for linea in f:
            existe = linea.strip().split(',')[0]
            if usuario == existe:
                return True
    return False

def Existe_rol(rol):
    with open('Roles/roles.txt', 'r') as f:
        for linea in f:
            existe = linea.strip().split(',')[0]
            if rol == existe:
                return True
    return False

def Asignar_rol(usuario, rol):
    with open('Datos/usuarios.txt', 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    nuevo_rol = []
    for linea in lineas:
        partes = linea.strip().split(',')
        if partes[0] == usuario:
            partes.append(rol)
            nuevo_rol.append(','.join(partes) + '\n')
            print(f'Rol asignado para: {usuario}\n')
        else:
            nuevo_rol.append(linea)
    
    with open('Datos/usuarios.txt', 'w', encoding='utf-8') as f:
        f.writelines(nuevo_rol)
    
def Eliminar_rol():
    usuario = input('Nombre del usuario al que le va a quitar el rol: ')
    with open('Datos/usuarios.txt', 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    restar_rol = []
    for linea in lineas:
        partes = linea.strip().split(',')
        if partes[0] == usuario and len(partes) > 3:
            partes = partes[:-1]
            restar_rol.append(','.join(partes) + '\n')
            Rol_eliminado = True
        else:
            restar_rol.append(linea)
    
    with open('Datos/usuarios.txt', 'w', encoding='utf-8') as f:
        f.writelines(restar_rol)
    
    if Rol_eliminado:
        print(f'Rol eliminado para: {usuario}')
    else:
        print(f'El usuario: {usuario} no tiene un rol asignado')

def Ver_roles():
    print('\n-----Roles-----')
    with open('Roles/roles.txt', 'r') as f:
        for linea in f:
            rol = linea.strip()
            print(f'- {rol}')

def Asignamiento_rol():
    usuario = input('Nombre del usuario: ')
    if Existe_usuario(usuario):
        Ver_roles()
        rol = input('\nRol a elegir: ')
        if Existe_rol(rol):
            Asignar_rol(usuario, rol)
        else:
            print('El rol no existe en la base de datos')
    else:
        print('Usuario no encontrado!')

def Menu_usuarios():
    while True:
        print('\n----menu----')
        print('1. Ver usuarios')
        print('2. Asignar rol')
        print('3. Eliminar rol')
        print('4. Salir')
        try:
            opcionUser = int(input('Que desea hacer: '))
            print('\n')
        except ValueError:
            print('Por favor ingrese un numero valido!\n')
            continue
        
        if opcionUser == 1:
            Ver_usuarios()

        elif opcionUser == 2:
            Asignamiento_rol()

        elif opcionUser == 3:
            Eliminar_rol()

        elif opcionUser == 4:
            print('Saliendo...')
            break

        else:
            print('Opcion no valida!')

def Menu_admin():
    while True:
        print('\n--------menu--------')
        print('1. Ver productos')
        print('2. Agrear productos')
        print('3. Actualizar productos')
        print('4. Eliminar productos')
        print('5. Consultar productos con stock bajo')
        print('6. Administrar usuarios')
        print('7. Salir')
        try:
            opcion = int(input('Que deseas hacer: '))
            print('\n')
        except ValueError:
            print('Por favor ingrese una opcion valida!')
            continue

        if opcion == 1:
            prod.Ver_productos()

        elif opcion == 2:
            prod.Agregar_producto()

        elif opcion == 3:
            prod.Actualizar_producto()

        elif opcion == 4:
            prod.Eliminar_producto()

        elif opcion == 5:
            Stock_bajo()

        elif opcion == 6:
            Menu_usuarios()

        elif opcion == 7:
            print('Hasta la proxima!')
            break

        else:
            print('Opcion no valida!')  

usuarioAdmin = 'El admin123'
contraAdmin = 'contra_admin'  