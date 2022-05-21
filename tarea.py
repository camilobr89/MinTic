"""
Realizar un programa en Python que pida:
-	Código del articulo
-	Nombre del articulo
-	Precio unitario con IVA del articulo
-	Porcentaje del IVA
El equipo de desarrolladores debe definir, si lo almacena en una lista, diccionario, archivo plano o archivo json y lo anteriormente expuesto debe estar en una función que permita capturar los diferentes artículos.
Posteriormente esos datos almacenados en otra función deben solicitar el código del articulo y traer los elementos correspondientes, paso a seguir el programa le debe permitir capturar la cantidad y calcular el subtotal sin IVA, el IVA y el total de los artículos que ha decidido capturar 
Por último una tercera función que me va a sacar la factura con todos los artículos, sub totales y al finalizar        
por último una tercera función que va asacar la factura con todos los artículos que he facturado con los subtotales y al finalizar el total del valor sin IVA y el total total con IVA, integrarse desde un menú, capturar artículos, facturar, mostrar factura


"""



articulos = {}

def capturar_articulos():
    """Capturar articulos"""
    codigo = input('Ingrese el codigo del articulo: ')
    articulos[codigo] = {}
    articulos[codigo]['nombre'] = input('Ingrese el nombre del articulo: ')
    articulos[codigo]['precio con IVA'] = float(input('Ingrese el precio unitario con IVA: '))
    articulos[codigo]['iva'] = float(input('Ingrese el porcentaje del IVA: '))

def facturar():
    """Facturar"""
    codigo = input('Ingrese el codigo del articulo: ')
    articulos[codigo]['cantidad'] = int(input('Ingrese la cantidad: '))
    if articulos[codigo]['cantidad'] < 0:
        print('La cantidad no puede ser negativa')
        return
    
    articulos[codigo]['subtotal sin IVA'] = articulos[codigo]['precio con IVA'] / (articulos[codigo]['iva'] / 100 + 1) * articulos[codigo]['cantidad']
    articulos[codigo]['subtotal con IVA'] = articulos[codigo]['cantidad'] * articulos[codigo]['precio con IVA']
    articulos[codigo]['iva'] = articulos[codigo]['subtotal sin IVA'] * articulos[codigo]['iva'] / 100
    # articulos[codigo]['iva'] = articulos[codigo]['subtotal con IVA'] * articulos[codigo]['iva'] / 100
    articulos[codigo]['total'] = articulos[codigo]['subtotal con IVA'] + articulos[codigo]['iva']
    

def mostrar_factura():
    """Mostrar factura"""
    print('Factura:')
    for articulo in articulos:
        print('Articulo: ', articulos[articulo]['nombre'])
        print('Cantidad: ', articulos[articulo]['cantidad'])
        print('Subtotal sin IVA: ', articulos[articulo]['subtotal sin IVA'])
        print('Subtotal con IVA: ', articulos[articulo]['subtotal con IVA'])
        print('IVA: ', articulos[articulo]['iva'])
        print('Total: ', articulos[articulo]['total'])
        print('\n')
        print('-----------------------------------------------------')
        
 

def run():
    """Menu de opcones:
    1. Capturar articulos
    2. Facturar
    3. Mostrar factura
    4. Salir
    """
    while True:
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
            capturar_articulos()
        elif opcion == "2":
            facturar()
        elif opcion == "3":
            mostrar_factura()
        elif opcion == "4":
            break
        else:
            print('Opción no valida')
    
print('-----------------------------------------------------')
print('Bienvenido al programa de facturación')
print('-----------------------------------------------------')
print('\n')
run()