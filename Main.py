from roles.Admin import Menu_admin
from roles.Clientes import Menu_cliente
from roles.Empleados import Menu_empleado

while True:
    print('\n---Como quieres acceder---')
    print('1. Cliente')
    print('2. Empleado')
    print('3. Administrador')
    print('4. Salir')
    try:
        opcion = int(input('Ingrese su opcion: '))
        print('\n')
    except ValueError:
        print('Por favor ingrese una opcion valida!')
        continue

    if opcion == 1:
        print()
