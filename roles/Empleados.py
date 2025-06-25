import Productos as prod

def Menu_empleado(rol):
    while True:
        print('\n---------menu--------')
        print('1. Ver productos')
        print('2. Vender productos')
        print('3. Historial de ventas')
        print('4. Salir')
        try:
            opcion = int(input('Que deseas hacer: '))
            print('\n')
        except ValueError:
            print('Por favor ingrese un numero valido!')
            continue 
        
        if opcion == 1:
            prod.Ver_productos()
    
        elif opcion == 2: 
            prod.Vender_producto()
    
        elif opcion == 3:
            prod.Historial_ventas()
    
        if opcion == 4:
            print('Hasta la proxima!')
            break
        
        else:
            print('Opcion no valida!')

contraEmpleado = 'contra_empleado'