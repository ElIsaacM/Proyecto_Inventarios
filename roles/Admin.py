import Productos as prod

def Stock_bajo():
    for nombre, datos in prod.productos.items():
        if datos['stock'] <= 10:
            print(f'{nombre}: Stock = {datos['stock']}')

def Menu_admin():
    while True:
        print('\n--------menu--------')
        print('1. Ver productos')
        print('2. Agrear productos')
        print('3. Actualizar productos')
        print('4. Eliminar productos')
        print('5. Consultar productos con stock bajo')
        print('6. Salir')
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
            print('Hasta la proxima!')
            break

        else:
            print('Opcion no valida!')  

contraAdmin = 'contra_admin'     