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

c = float(input("Ingrese el centro del cırculo: "))
r = float(input("Ingrese el radio del cırculo: "))

def circulo(c, r):
    x = float(input("Ingrese el punto x: "))
    y = float(input("Ingrese el punto y: "))

    if (x - c)**2 + (y - c)**2 <= r**2:
        return ("El punto esta dentro del cırculo")
    else:
        return ("El punto esta fuera del cırculo")

print(circulo(c, r))

###############################################################################




















