def ajustar_len(texto, longitud):
    return (texto * ((longitud // len(texto)) + 1))[:longitud]

def Encriptar(contrasena, clave):
    max_len = max(len(contrasena), len(clave))
    contrasena = ajustar_len(contrasena, max_len)
    clave = ajustar_len(clave, max_len)

    valorAscii = []
    for i in range(len(contrasena)):
        suma = ord(contrasena[i]) + ord(clave[i])
        valorAscii.append(suma)

    convertir = ''
    for valor in valorAscii:
        if 0 <= valor <= 1114111:
            convertir += chr(valor)
        else:
            convertir += '?'
    return convertir

def Desencriptar(convertir, clave):
    clave = ajustar_len(clave, len(convertir))
    revertirAscii = []
    for i in range(len(convertir)):
        resta = ord(convertir[i]) - ord(clave[i])
        revertirAscii.append(resta)

    revertir = ''
    for valor in revertirAscii:
        if 0 <= valor <= 1114111:
            revertir += chr(int(valor))
        else:
            revertir += '?'
    return revertir

'''def Menu_encriptar():
    Contrasena = input('Ingrese una contraseña: ')
    clave = input('Ingresa una clave de recuperacion: ')
    
    while True:
        print('\n-----menu----')
        print('1. Encriptar contraseña')
        print('2. Desencriptar contraseña')
        print('3. Salir')
        try:
            opcion = int(input('Que deseas hacer: '))
            print('\n')
        except ValueError:
            print('Opcion no valida!')
            continue
        
        if opcion == 1:
            convertir = Encriptar(Contrasena, clave)
            print(f'La contraseña encriptada es: {convertir}')
    
        if opcion == 2:
            if convertir is None:
                print('No has encriptado tu contraseña')
                continue
            TuClave = input('Ingresa tu clave de recuperacion: ')
            if TuClave == clave:
                contrasenaDesencriptada = Desencriptar(convertir, clave)
                print(f'La contraseña desencriptada es: {contrasenaDesencriptada}')
            else:
                print('Clave incorrecta!')
    
        if opcion == 3:
            break'''