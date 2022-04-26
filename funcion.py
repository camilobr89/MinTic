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
#     total = b - (p * PANES + l * LECHE + h * HUEVOS)
#     return total
# print("La cantidad de vueltas o deuda de compra del pan es: $", vueltas(b, p, l, h))

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

peso = int(input("Ingresa el peso de Ale: "))


def vascula(peso):
    gi = (peso * 2) + 4
    nico = (peso + gi) / 5

    print(peso, gi, nico.__int__())
    
    if nico > 0 and nico < 20:
        return "uno"
    elif nico > 21 and nico < 40:
        return "dos"
    elif nico > 41 and nico < 80:
        return "tres"
    else:
        return "cuatro"


print(vascula(peso))

###############################################################################


    

    














