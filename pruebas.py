# Se le solicita elaborar de manera individual un programa en python que: 
# 1- Cuantos productos va a facturar 2- Debe mandar ese elemento a una función donde va a solicitar: - Nombre del articulo - Precio del articulo sin IVA - Cantidad - Porcentaje del IVA 3- Calcula por cada articulo - El subtotal sin Iva - El valor del IVA - Total con IVA 4- Adicionalmente debe acumular todos los subtotales, todos los valores del IVA y todos los totales de los productos. 5- El gerente comercial buscando incremen
# 5- El gerente comercial buscando incrementar las ventas ofrece: - Si el total de la factura supera 5 millones se le da el 10% al subtotal - Si el total de la factura supera 2 millones se le da el 3% al subtotal - Si el total de la factura supera 1 millones se le da el 1% al subtotal - Para otro valor no se da descuento 

def facturacion(nombre, precio, cantidad, iva):
    subtotal = precio * cantidad
    iva = subtotal * iva
    total = subtotal + iva
    return subtotal, iva, total

    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))
        iva = float(input("Ingrese el porcentaje del IVA: "))
        subtotal, iva, total = facturacion(nombre, precio, cantidad, iva)
        print("El subtotal es: ", subtotal)
        print("El valor del IVA es: ", iva)
        print("El total es: ", total)
        print("Desea continuar? S/N")
        opcion = input()
        if opcion == "N":
            break
        else:
            continue


