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

import json




def capturar_articulos():
    """Se captura los datos del articulo:
       1. Código del articulo
       2. Nombre del articulo
       3. Precio unitario con IVA del articulo
       4. Porcentaje del IVA
    """
    
    global articulos
    
    codigo = json.loads(input('Ingrese el código del artículo: '))
    nombre = json.loads(input('Ingrese el nombre del artículo: '))
    precio = json.loads(float(input('Ingrese el precio del artículo con IVA incluido: ')))
    iva = json.loads(float(input('Ingrese el porcentaje del IVA: ')))
    articulos[codigo] = {"nombre": nombre, "precio": precio, "iva": iva}
    


def facturar():
    """Se pedira nuevamente el codigo del articulo y se mostrara el subtotal sin IVA, el IVA y el total de los artículos que ha decidido capturar 
    """
    global articulos
    codigo = json.loads(input('Ingrese el código del artículo: '))
    if codigo in articulos:
        print('Subtotal sin IVA: ', articulos[codigo]['precio'] * articulos[codigo]['iva'])
        print('IVA: ', articulos[codigo]['precio'] * articulos[codigo]['iva'])
        print('Total: ', articulos[codigo]['precio'] * articulos[codigo]['iva'] * articulos[codigo]['iva'])
    else:
        print('El código no existe')
    
def mostrar_factura():
    """Se mostrara la factura con todos los artículos que he facturado con los subtotales y al finalizar el total del valor sin IVA y el total total con IVA, integrarse desde un menú, capturar artículos, facturar, mostrar factura
    """
    print('Factura:')
    print('Artículos:')
    for articulo in articulos:
        print(articulo)
    print('Subtotales:')
    for articulo in articulos:
        print(articulo)
    print('Total:')
    for articulo in articulos:
        print(articulo)
    
 

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
        print('4. Salir')
        opcion = json.loads(input('Ingrese una opción: '))
        if opcion == 1:
            capturar_articulos()
        elif opcion == 2:
            facturar()
        elif opcion == 3:
            print(articulos)
        elif opcion == 4:
            break
        else:
            print('Opción no valida')
    

print('Bienvenido al programa de facturación')
run()