productos = {
    'pan': {'precio': 1000, 'stock': 20},
    'leche': {'precio': 3500, 'stock': 15},
}

Hist_ventas = []

def Ver_Prod():
    for nombre, data in productos.items():
        print(f'{nombre}: ${data['precio']}')
        print(f'Stock = {data['stock']}\n')        

def menu_cliente():
    Ver_Prod()

def menu_empleado():
    while True:
        print('\n----menu----')
        print('1. Ver producto')
        print('2. Vender producto')
        print('3. Salir')
        opcionEmpleado = int(input('Que deseas hacer: '))
        print('\n')

        if opcionEmpleado == 1:
            Ver_Prod()

        elif opcionEmpleado == 2:
            vender = input('\nNombre del producto: ')
            if vender in productos:
                cantidad = int(input('Cantidad a vender: '))
                if cantidad <= productos[vender]['stock']:
                    stock = productos[vender]['stock']
                    productos[vender]['stock'] = stock - cantidad
                    print('\nVenta exitosa')
                    subtotal = productos[vender]['precio'] * cantidad
                    Hist_ventas.append({'producto': vender, 'cantidad': cantidad, 'subtotal': subtotal})
                else:
                    print('Cantidad no disponible!')
            else:
                print('Producto no disponible!')
        
        elif opcionEmpleado == 3:
            Ver_Historial()
            print('Hasta la proxima!')
            break
        
        else: 
            print('Opcion invalida!')

def Ver_Historial():
    for venta in Hist_ventas:
        print(f'{venta['producto']}: Cantidad = {venta['cantidad']}')
        print(f'Subtotal = ${venta['subtotal']}\n')

def menu_admin():
    while True:
        print('\n----menu----')
        print('1. Ver Productos')
        print('2. Agregar Producto')
        print('3. Actualizar produto')
        print('4. Salir')
        opcionAdmin = int(input('Que deseas hacer: '))
        print('\n')

        if opcionAdmin == 1:
            Ver_Prod()
        
        elif opcionAdmin == 2:
            nombre = input('Nombre del producto: ')
            if nombre in productos:
                print('Ya existe el producto en el inventario!')
            else:
                precio = int(input('Precio del producto: '))
                cantidad = int(input('Cantidad de stock: '))

                productos[nombre] = {'precio': precio, 'stock': cantidad}
                print('\nAgregado exitosamente')

        elif opcionAdmin == 3:
            nombre = input('Nombre del producto: ')
            if nombre in productos:
                ACT_precio = int(input('Precio del producto: '))
                ACT_cantidad = int(input('Cantidad de stock: '))

                productos[nombre] = {'precio': ACT_precio, 'stock': ACT_cantidad}
                print('\nActualizado exitosamente')
            else:
                print('Producto no disponible en el stock!')

        elif opcionAdmin == 4:
            print('Hasta la poxima!')
            break

        else:
            print('Opcion invalida!')

while True:
    print('\n----menu----')
    print('1. Cliente')
    print('2. Empleado')
    print('3. Administrador')
    print('4. Salir')
    try:
        opcion = int(input('Digite su rol: '))
        print('\n')
    except ValueError:
        print('Ingrese un numero valido!')
        continue

    if opcion == 1:
        menu_cliente()

    elif opcion == 2:
        contrasena = 'contra_empleado'
        ingContrasena = input('Ingresa tu contraseña: ')
        if ingContrasena == contrasena:
            print('hola empleado\n')
            menu_empleado()
        else:
            print('Contraseña invalida!')

    elif opcion == 3:
        contrasena = 'contra_admin'
        ingContrasena = input('Ingresa tu contraseña: ')
        if ingContrasena == contrasena:
            print('hola admin\n')
            menu_admin()
        else:
            print('Contraseña invalida!')

    elif opcion == 4:
        print('hasta la proxima!')
        break

    else:
        print('Opcion invalida!')