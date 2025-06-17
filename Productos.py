productos = {
    'pan': {'precio': 1000, 'stock': 20},
    'leche': {'precio': 3500, 'stock': 15},
}

# ver producto
def Ver_productos():
    for nombre, datos in productos.items():
        print(f'{nombre}: ${datos['precio']} / cantidad = {datos['stock']}')

# Agregar producto
def Agregar_producto():
    nombre = input('Nombre del producto: ')
    if nombre in productos:
        print('\nYa existe el producto en el inventario')
        opcionAGG = input('Deseas actualizarlo s/n: ')
        if opcionAGG == 's':
            Actualizar_producto()
        else: 
            print('...')
    else:
        precio = int(input('Precio del producto: '))
        cantidad = int(input('Cantidad de stock: '))

        productos[nombre] = {'precio': precio, 'stock': cantidad}
        print('\nProducto agregado con exito!')

# Actualizar producto
def Actualizar_producto():
    nombre = input('Nombre del producto: ')
    if nombre in productos:
        ACT_precio = int(input('Precio del producto: '))
        ACT_cantidad = int(input('Cantidad de stock: '))

        productos[nombre] = {'precio': ACT_precio, 'stock': ACT_cantidad}
        print('\nProducto actualizado con exito!') 

# Eliminar Producto
def Eliminar_producto():
    nombre = input('Nombre del producto: ')
    if nombre in productos:
        del productos[nombre]
        print('Producto eliminado con exito!')

# Validar existencia
def Existe_producto(nombre):
    return nombre in productos

# Validar si hay stock suficiente
def Stock_disponible(nombre, cantidad):
    return productos[nombre]['stock'] >= cantidad

from datetime import datetime

# Vender producto (descontar del stock)
def Vender_producto():
    nombre = input('Nombre del producto: ')
    if Existe_producto(nombre):
        cantidad = int(input('Cantidad: '))
        if Stock_disponible(nombre, cantidad):
            productos[nombre]['stock'] -= cantidad
            print(f'\n{cantidad} unidades de {nombre} vendidas.')
            fecha = datetime.now()
            HistorialVentas.append({'producto': nombre, 'stock': cantidad, 'fecha': fecha})
        else: 
            print(f'\nNo hay suficiente stock de {nombre}')
    else:
        print(f'\nNo existe el producto {nombre}.')

HistorialVentas = []

def Historial_ventas():
    if not HistorialVentas:
        print('No hay ventas registradas')
    else:
        for venta in HistorialVentas:
            print(f'{venta['producto']}: {venta['stock']} uds\n{venta['fecha']}\n')