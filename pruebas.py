# Se le solicita elaborar de manera individual un programa en python que: 
# 1- Cuantos productos va a facturar 2- Debe mandar ese elemento a una función donde va a solicitar: - Nombre del articulo - Precio del articulo sin IVA - Cantidad - Porcentaje del IVA 3- Calcula por cada articulo - El subtotal sin Iva - El valor del IVA - Total con IVA 4- Adicionalmente debe acumular todos los subtotales, todos los valores del IVA y todos los totales de los productos. 5- El gerente comercial buscando incremen
# 5- El gerente comercial buscando incrementar las ventas ofrece: - Si el total de la factura supera 5 millones se le da el 10% al subtotal - Si el total de la factura supera 2 millones se le da el 3% al subtotal - Si el total de la factura supera 1 millones se le da el 1% al subtotal - Para otro valor no se da descuento 


subTotal = 0
i = 0

productos = int(input("Cuantos productos va a facturar: "))

while i < productos:
    nombre = input("Nombre del articulo: ")
    precio = float(input("Precio del articulo sin IVA: "))
    cantidad = int(input("Cantidad: "))
    porcentaje = float(input("Porcentaje del IVA: "))
    subtotal = precio * cantidad
        
    subTotal += subtotal
    iva = subTotal * porcentaje
    total = subTotal + iva
    i += 1
    print("Subtotal: $%d" %subTotal)
    print("Total con IVA: $%d" %total)
    print("IVA: $%d" %iva, end="\n\n")

if total > 5000000:
    total -= subTotal * 0.10
    print("El total de la factura con un descuento del 10 porciento es: $%d" %total)
elif total > 2000000:
    total -= subTotal * 0.03
    print("El total de la factura con un descuento del 3 porciento es: $%d" %total)
elif total > 1000000:
    total -= subTotal * 0.01
    print("El total de la factura con un descuento del 1 porciento es: $%d" %total)
else:
    total = total
    print("El total de la factura es: $%d" %total)







