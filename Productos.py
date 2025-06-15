productos = {
    'pan': {'precio': 1000, 'stock': 20},
    'leche': {'precio': 3500, 'stock': 15},
}

# ver producto
def Ver_productos():
    for nombre, datos in productos.items():
        print(f'{nombre}: ${datos['precio']} / cantidad = {datos['stock']}')

# Agregar producto

# Actualizar producto

# Eliminar Producto

# Stock

# Existencia

# Descontar / vender