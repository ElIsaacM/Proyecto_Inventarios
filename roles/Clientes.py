import Productos as prod 

carrito = {}

#agregar al carrito / ver productos
def Agregar_carrito():
    producto = input('Nombre del producto: ')
    if producto in prod.productos:
        cantidad = int(input('Cuantos vas a agregar: '))
        if cantidad <= prod.productos[producto]['stock']:
            print('\nProducto agegado con exito!')
            print(f'Stock restante: {producto} = ${prod.productos[producto]['precio']} / {prod.productos[producto]['stock'] - cantidad} uds\n')
            if producto in carrito:
                carrito[producto] += cantidad
            else:
                carrito[producto] = cantidad
        else:
            print('No hay suficiente stock del producto!')
    else:
        print('Producto no disponible!')

#confirmar compra / ver carrito
def Ver_carrito():
    total = 0
    for producto, cantidad in carrito.items():
        precio_unidad = prod.productos[producto]['precio']
        subtotal = precio_unidad * cantidad
        print(f'{producto} x {cantidad}: Precio = {precio_unidad}')
        print(f'Subtotal = {subtotal}\n')
        total += subtotal
    print(f'Total = {total}')

def Confirmar_carrito():
    Confirmar = input('Desea confirmar la compra s/n: ')
    print('\n')
    if Confirmar == 's':
        print('Gracias, hasta la proxima!')
        for producto, cantidad in carrito.items():
            prod.productos[producto]['stock'] -= cantidad
        return True
    else:
        print('Puedes agregar mas productos')
        return False

def Menu_cliente():
    while True:
        print('\n--------menu--------')
        print('1. Ver productos')
        print('2. Agregar al carrito')
        print('3. Ver carrito / comprar')
        print('4. Salir')
        try:
            opcionCliente = int(input('Que deseas hacer: '))
            print('\n')
        except ValueError:
            print('Por favor ingrese un numero valido')
            continue
        
        if opcionCliente == 1:
            prod.Ver_productos()
    
        elif opcionCliente == 2:
            Agregar_carrito()
    
        elif opcionCliente == 3:
            print('Tu carrito es:\n')
            Ver_carrito()
            if Confirmar_carrito():
                break
            
        elif opcionCliente == 4:
            Ver_carrito()
            print('Hasta la proxima!') 
            break