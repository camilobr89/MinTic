# Calcula el area lateral del vagon


###############################################################################

# Diseñar una funcion que calcule la cantidad de carne de aves en kilos

# GALLINAS = 6
# GALLOS = 7
# POLLITOS = 1

# n = int(input("Ingrese la cantidad de gallinas: "))
# m = int(input("Ingrese la cantidad de gallos: "))
# k = int(input("Ingrese la cantidad de pollitos: "))

# def cantidad_carne(n, m, k):
#     total_kilos = n * GALLINAS + m * GALLOS + k * POLLITOS
#     return total_kilos
# print("La cantidad de carne en kilos es: ", cantidad_carne(n, m, k), "kg de carne de ave")

###############################################################################

# Calcular las vueltas o deuda de  compra del pan

# PANES = 300
# LECHE = 3300
# HUEVOS = 350

# b = int(input("Ingrese el valor del billete: "))
# p = int(input("Ingrese la cantidad de panes: "))
# l = int(input("Ingrese la cantidad de leche: "))
# h = int(input("Ingrese la cantidad de huevos: "))

# def vueltas(b, p, l, h):
#     total_vueltas = b - (p * PANES + l * LECHE + h * HUEVOS)
 
#     total_deuda = b - (p * PANES + l * LECHE + h * HUEVOS)
    
#     if total_deuda < 0:
#         print("Usted debe devolver: ", total_deuda, "pesos")
#     else:
#         print("Sus vueltas son: ", total_vueltas, "pesos")

# print(vueltas(b, p, l, h))


###############################################################################

# Valor absoluto:

# def valor_absoluto(x):
#     if x >= 0:
#         valor = x
#     else:
#         valor = -x
#     return valor

# x = float(input("Ingrese un n ́umero real x: "))
# valor_abs = valor_absoluto(x)
# print("El valor absoluto de " + str(x), end = " ")
# print("es " + str(valor_abs))

###############################################################################

# from math import pi
# def Volumen_total(R1,R2,H):
#     Esfera=(4*pi*R1**3)/3
#     Cono=(H*pi*R2**2)/3
    
#     Vt=Esfera+Cono

#     return Vt

# r1=float(input("Radio de la esfera: "))
# r2=float(input("Radio del cono: "))
# h=float(input("Altura del cono: "))

# print("El volumen total es: ", end="")
# print(Volumen_total(r1,r2,h))
# print("")
# print("")
# print("")
# print("Volumen de la esfera: ")
# print("Volumen del cono: ")

###############################################################################

# peso = int(input("Ingresa el peso de Ale: "))


# def vascula(peso):
#     gi = (peso * 2) + 4
#     nico = (peso + gi) / 5

#     print(peso, gi, nico.__int__())
    
#     if nico > 0 and nico < 20:
#         return "uno"
#     elif nico > 21 and nico < 40:
#         return "dos"
#     elif nico > 41 and nico < 80:
#         return "tres"
#     else:
#         return "cuatro"


# print(vascula(peso))

###############################################################################

# def nota_final(nota1):
#     nota2 = nota1 * 2
#     nota3 = (nota1 + nota2) / 2
#     nota4 = 20 * nota1 / 100
#     nota5 = (nota3 + nota4) * 4
#     nota_final = (nota1 * 0.10) + (nota2 * 0.15) + (nota3 * 0.20) + (nota4  * 0.25) + (nota5 * 0.30)

#     print(nota1, nota2, nota3, nota4, nota5)

#     if nota_final > 6 and nota_final < 7.6:
#         return "Aprobado"
#     elif nota_final > 7.6 and nota_final < 10:
#         return "Sobresaliente"
#     elif nota_final > 10:
#         return "Excelente"  
#     else:
#         return "Reprobado"


# nota1 = float(input("Ingrese la nota 1: "))
# print(nota_final(nota1))

###############################################################################

# nota1 = float(input("Nota 1: "))
# nota2 = nota1*2
# nota3 = (nota1+nota2)/2
# nota4 = nota1*0.20
# nota5 = (nota3+nota4)*4
# notaFinal = (nota1*0.10)+(nota2*0.15)+(nota3*0.20)+(nota4*0.25)+(nota5*0.30)

# print(nota1,nota2,nota3,nota4,nota5)

# if notaFinal>=10:
#     print("Super Excelente") 
# elif notaFinal>=7.6 and notaFinal<10:
#     print("Bueno")
# elif notaFinal>=6.0 and notaFinal<7.6:
#     print("Paso")
# else:
#     print("Reprobo")

###############################################################################

# Numeros primops

# def es_primo(numero):
#     contador = 0

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False

# def run():
#     numero = int(input("Ingrese un numero: "))
#     if es_primo(numero):
#         print("Es primo")
#     else:
#         print("No es primo")

# if __name__ == "__main__":
#     run()


###############################################################################

# Dadas tres longitudes positivas, determinar si con esas longitudes se
# puede construir un tri ́angulo.

# a = int(input("Ingrese la longitud de la primera lado: "))
# b = int(input("Ingrese la longitud de la segunda lado: "))
# c = int(input("Ingrese la longitud de la tercera lado: "))

# print(a, b, c)

# def triangulo(a, b, c):
#     if a < (b + c) and b < (a + c) and c < (a + b):
#         print("Es un triangulo")
#     else:
#         print("No es un triangulo")

# print(triangulo(a, b, c))

###############################################################################

# Dado el centro y el radio de un cırculo, determinar si un punto de R**2
# pertenece o no al interior del cırculo.

# c = float(input("Ingrese el centro del cırculo: "))
# r = float(input("Ingrese el radio del cırculo: "))

# def circulo(c, r):
#     x = float(input("Ingrese el punto x: "))
#     y = float(input("Ingrese el punto y: "))

#     if (x - c)**2 + (y - c)**2 <= r**2:
#         return ("El punto esta dentro del cırculo")
#     else:
#         return ("El punto esta fuera del cırculo")

# print(circulo(c, r))

###############################################################################

# Se le solicita elaborar de manera individual un programa en python que: 
# 1- Cuantos productos va a facturar 2- Debe mandar ese elemento a una función donde va a solicitar: - Nombre del articulo - Precio del articulo sin IVA - Cantidad - Porcentaje del IVA 3- Calcula por cada articulo - El subtotal sin Iva - El valor del IVA - Total con IVA 4- Adicionalmente debe acumular todos los subtotales, todos los valores del IVA y todos los totales de los productos. 5- El gerente comercial buscando incremen
# 5- El gerente comercial buscando incrementar las ventas ofrece: - Si el total de la factura supera 5 millones se le da el 10% al subtotal - Si el total de la factura supera 2 millones se le da el 3% al subtotal - Si el total de la factura supera 1 millones se le da el 1% al subtotal - Para otro valor no se da descuento 


# subTotal = 0
# i = 0

# productos = int(input("Cuantos productos va a facturar: "))

# while i < productos:
    # nombre = input("Nombre del articulo: ")
    # precio = float(input("Precio del articulo sin IVA: "))
    # cantidad = int(input("Cantidad: "))
    # porcentaje = float(input("Porcentaje del IVA: "))
    # subtotal = precio * cantidad
        
#     subTotal += subtotal
#     iva = subTotal * porcentaje
#     total = subTotal + iva
#     i += 1
#     print("Subtotal: $%d" %subTotal)
#     print("Total con IVA: $%d" %total)
#     print("IVA: $%d" %iva, end="\n\n")

# if total > 5000000:
#     total -= subTotal * 0.10
#     print("El total de la factura con un descuento del 10 porciento es: $%d" %total)
# elif total > 2000000:
#     total -= subTotal * 0.03
#     print("El total de la factura con un descuento del 3 porciento es: $%d" %total)
# elif total > 1000000:
#     total -= subTotal * 0.01
#     print("El total de la factura con un descuento del 1 porciento es: $%d" %total)
# else:
#     total = total
#     print("El total de la factura es: $%d" %total)

###############################################################################


# def facturacion():
#     subTotal = 0
#     i = 0
#     nombre = []
#     productos = int(input("Cuantos productos va a facturar: "))

#     while i < productos:
        
#         nombre.append(input("Nombre del articulo: "))
#         precio = float(input("Precio del articulo sin IVA: "))
#         cantidad = int(input("Cantidad: "))
#         porcentaje = float(input("Porcentaje del IVA: "))
#         subtotal = precio * cantidad
#         subTotal += subtotal
#         iva = subTotal * (porcentaje / 100)
#         total = subTotal + iva
#         i += 1
#         print("Los articulo en la lista actual son: %s" %nombre)
#         print("Subtotal: $%d" %subTotal)
#         print("Total con IVA: $%d" %total)
#         print("IVA: $%d" %iva, end="\n\n")
    
#     if total > 5000000:
#         total -= subTotal * 0.10
#         print("El total de la factura con un descuento del 10 porciento es: $%d" %total)
#     elif total > 2000000:
#         total -= subTotal * 0.03
#         print("El total de la factura con un descuento del 3 porciento es: $%d" %total)
#     elif total > 1000000:
#         total -= subTotal * 0.01
#         print("El total de la factura con un descuento del 1 porciento es: $%d" %total)
#     else:
#         total = total
#         print("El total de la factura es: $%d" %total)
    
    


# if __name__ == "__main__":
#     facturacion()
   
###############################################################################


# def minmax(a, b):
#     if a < b:
#         return a, b
#     else:
#         return b, a

# x, y = minmax(5,13)

# print("min =", x, ",", "max = ", y)
# x, y = minmax(12, -4)
# print("min =", x, ",", "max =", y)

####################

t = tuple(map(int, input().split()))
print(t)
print(t[0])
print(t[3])















