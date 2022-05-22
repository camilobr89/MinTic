"""
Realizar un programa en Python que pida:
-	Código del articulo
-	Nombre del articulo
-	Precio unitario con IVA del articulo
-	Porcentaje del IVA
El equipo de desarrolladores debe definir, si lo almacena en una lista, diccionario, archivo plano o archivo json y lo anteriormente expuesto debe estar en una función que permita capturar los diferentes artículos.
Posteriormente esos datos almacenados en otra función deben solicitar el código del articulo y traer los elementos correspondientes, paso a seguir el programa le debe permitir capturar la cantidad y calcular el subtotal sin IVA, el IVA y el total de los artículos que ha decidido capturar 
    
por último una tercera función que va asacar la factura con todos los artículos que he facturado con los subtotales y al finalizar el total del valor sin IVA y el total total con IVA, integrarse desde un menú, capturar artículos, facturar, mostrar factura


"""
articulos = {}                          # Diccionario de articulos

def capturar_articulos():               # Funcion para capturar los articulos
    """Capturar articulos"""
    codigo = input('Ingrese el codigo del articulo: ')
    articulos[codigo] = {}              # Creacion de un diccionario para almacenar los articulos
    articulos[codigo]['nombre'] = input('Ingrese el nombre del articulo: ')  # Captura del nombre del articulo
    articulos[codigo]['precio con IVA'] = float(input('Ingrese el precio unitario con IVA: $')) # Captura del precio con IVA
    articulos[codigo]['iva'] = float(input('Ingrese el porcentaje del IVA: '))   # Captura del porcentaje del IVA
    print('-----------------------------------------------------')
    print('\n')    

def facturar():                    # Funcion para facturar
    """Facturar"""
    codigo = input('Ingrese el codigo del articulo: ')  # Captura del codigo del articulo previamente capturado
    articulos[codigo]['cantidad'] = int(input('Ingrese la cantidad: '))   # Captura de la cantidad
    print('\n')
    print('-----------------------------------------------------')
    
    if articulos[codigo]['cantidad'] < 0:            # Validacion de la cantidad ingresada, no puede ser negativa
        print('La cantidad no puede ser negativa')
        return

    total_sin_iva = 0                      # Inicializacion de variables total sin iva
    tota_general = 0                       # Inicializacion de variables total general con iva
    
    articulos[codigo]['subtotal sin IVA'] = articulos[codigo]['precio con IVA'] / (articulos[codigo]['iva'] / 100 + 1) * articulos[codigo]['cantidad']     # Calculo del subtotal sin iva
    articulos[codigo]['iva'] = articulos[codigo]['subtotal sin IVA'] * articulos[codigo]['iva'] / 100    # Calculo del iva
    articulos[codigo]['subtotal con IVA'] = articulos[codigo]['cantidad'] * articulos[codigo]['precio con IVA']     # Calculo del subtotal con iva
    
    for articulo in articulos:        # Ciclo para calcular el total sin iva de todos los articulos
        total_sin_iva += articulos[articulo]['subtotal sin IVA']
    articulos[codigo]['total sin IVA'] = total_sin_iva   

    for articulo in articulos:        # Ciclo para calcular el total general de todos los articulos
        tota_general += articulos[articulo]['subtotal con IVA']
    articulos[codigo]['total'] = tota_general
    


def mostrar_factura():               # Funcion para mostrar la factura
    """Mostrar factura"""
    print('Factura:')
    for articulo in articulos:       # Ciclo para mostrar la factura final, imprime los calculos realizados en la funcion facturar e imprime los articulos capturados en la funcion capturar_articulos
        print('Articulo: ', articulos[articulo]['nombre'])
        print('Cantidad: ', articulos[articulo]['cantidad'])
        print('Subtotal sin IVA: $%d' %articulos[articulo]['subtotal sin IVA'])
        print('IVA: $%d' %articulos[articulo]['iva'])
        print('Subtotal con IVA: $%d' %articulos[articulo]['subtotal con IVA'])
        print('\n')
        print('-----------------------------------------------------')
    print('Total sin IVA: $%d' %articulos[articulo]['total sin IVA'])           
    print('Total con IVA: $%d' %articulos[articulo]['total'])
    print('-----------------------------------------------------')
    print('\n')
        
 

def run():                              # Funcion principal
    """Menu de opcones:
    1. Capturar articulos
    2. Facturar
    3. Mostrar factura
    4. Salir
    """
    while True:                             # Ciclo infinito hasta que el usuario ingrese la opcion 4
        print('Menu de opciones:')    
        print('1. Capturar articulos')
        print('2. Facturar')
        print('3. Mostrar factura')                 
        print('4. Salir\n')
        print('-----------------------------------------------------')
        opcion = input('Ingrese una opción: ')
        print('-----------------------------------------------------')
        print('\n')
        if opcion == "1":
            capturar_articulos()             # Llamada a la funcion capturar_articulos
        elif opcion == "2":
            facturar()                       # Llamada a la funcion facturar
        elif opcion == "3":
            mostrar_factura()                # Llamada a la funcion mostrar_factura
        elif opcion == "4":
            break
        else:
            print('Opción no valida')
    
print('-----------------------------------------------------')
print('Bienvenido al programa de facturación')                  # Banner de bienvenida
print('-----------------------------------------------------')
run()                                                           # Función que corre el programa