# # 1. Ejercicio 1

# # Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triangulo.
# # Teorema de Pitágoras H2 = A2 + B2
# # lado a, lado b y lado c

# #si a < (b + c)
# #si b < (a + c)
# #si c < (a + b)


# longitud_a = int(input("Introducir longitud a: "))
# longitud_b = int(input("Introducir longitud b: "))
# longitud_c = int(input("Introducir longitud c: "))

# print(longitud_a,longitud_b,longitud_c)

# if longitud_a <(longitud_b + longitud_c):
#   print("es un triangulo")

# elif longitud_b <(longitud_a + longitud_c):
#   print("es un triangulo")

# elif longitud_c <(longitud_a + longitud_b):
#   print("es un triangulo")

# else:
#   print("no es un triangulo")

# ###############################################################################

# # Ejercicio 2
# # Dado el centro y el radio de un circulo, determinar si un punto de R2 pertenece o no al interior del circulo.

# cx = float(input("Ingrese la coordenada en X del centro del circulo: "))
# cy = float(input("Ingrese la coordenada en y del centro del circulo: "))
# r = float(input("Ingrese el radio del circulo: "))


# def circulo(cx,cy,r):
#     x = float(input("Ingrese el punto x: "))
#     y = float(input("Ingrese el punto y: "))

#     if (x - cx)*2 + (y - cy)**2 <= r*2:
#         return "El punto esta dentro del circulo"
#     else:
#         return"El punto esta fuera del circulo"
    
# print(circulo(cx,cy,r))

# ###############################################################################

# # Ejercicio 3

# # Mi mam ́a me manda a comprar P panes a $ 300 cada uno, M bolsas
# # de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
# # programa que me diga las vueltas (o lo que quedo debiendo) cuando
# # me da un billete de B pesos.

def deuda(b, p, l, h):
    PANES = 300
    LECHE = 3300
    HUEVOS = 350

    return b - (p * PANES + l * LECHE + h * HUEVOS)

def run():
    b = int(input("Ingrese el valor del billete: " + "$"))
    p = int(input("Ingrese la cantidad de panes: "))
    l = int(input("Ingrese la cantidad de leche: "))
    h = int(input("Ingrese la cantidad de huevos: "))

    if deuda(b, p, l, h) < 0:
        print("Usted debe devolver $%d pesos" % abs(deuda(b, p, l, h)))
    else:
        print("Sus vueltas son: $%d pesos" % deuda(b, p, l, h))

if __name__ == "__main__":
    run()

###############################################################################

#Ejercicio 4

# Si pido prestados P cantidad de pesos para pagarlos en dos meses, si
# el interes del prestamo es del 3% al mes. >Cuanto se debe pagar al
# final del segundo mes si el interes es compuesto mensualmente?.

# p = int(input("Ingrese la cantidad de pesos a pagar: "))
# INTERES = 0.03

# total = p * (1 + INTERES)**2

# print("El total a pagar es: $%d" % total)

# ###############################################################################

# # Ejercicio 5

#Al granjero se le daño el corral y no sabe si volver a cercar el corral
#con madera, alambre de puas o poner reja de metal. Si va a cercar
#con madera debe poner 4 hileras de tablas, con varilla 8 hileras y con
#alambre solo 5 hileras, el quiere saber que es lo menos costoso para
#cercar si sabe que el alambre de puas vale P por metro, las tablas a Q
#por metro y las varillas S por metro. Dado el tamaño del corral y los
#precios de los elementos, > cual cerramiento es el mas economico?.


# Total_hojas=int(input("¿Cuantas hojas desea obtener?"))
# Hojas=int(input("¿Cuantas hojas tiene cada rama?"))
# ramas=int(input("¿Cuantas ramas tiene cada arbol?"))

# def Num_arboles(T,H,r):
#   r_necesarias=T/H
#   A=r_necesarias//r
#   return A
# residuo=(Total_hojas-(Num_arboles(Total_hojas,Hojas,ramas)*ramas*Hojas))//Hojas
# hojitas= residuo%Hojas
# if residuo==0:
#   print("Necesita podar %.2f arboles para obtener %.2f hojas" % (Num_arboles(Total_hojas,Hojas,ramas), Total_hojas))
# elif hojitas==0:
#   print("Necesita podar %.2f arboles para obtener %.2f hojas" % (Num_arboles(Total_hojas,Hojas,ramas), Total_hojas))

# elif hojitas==0:
#   print("Necesita podar %.2f arboles y %.2f ramas para obtener %.2f hojas" % (Num_arboles(Total_hojas,Hojas,ramas),residuo, Total_hojas))
# else:
#   print("Necesita podar %.2f arboles, %.2f ramas y %.2f hojitas para obtener %.2f hojas" % (Num_arboles(Total_hojas,Hojas,ramas),residuo,hojitas, Total_hojas))


###############################################################################

# El numero de contagiados de Covid-19 en el paıs de NuncaLandia se
# duplica cada dıa. Hacer un programa que diga el numero total de
# personas que se han contagiado cuando pasen D dıas a partir de hoy,
# si el numero de contagiados actuales es C

# D = int(input("Ingrese los dias que pasaron: "))
# C = int(input("Ingrese el numero de contagiados actuales: "))

# num_total = C * (2 ** D)

# print("El numero total de contagiados es: %d" % num_total)

###############################################################################

# si una vaca necesita K metros cuadrados de pasto para producir x
# litros de leche por dia, ¿cuantos litros de leche se producen por 
# semana en la granja?

# k = int(input("Ingrese los metros cuadrados de pasto: "))
# x = int(input("Ingrese los litros de leche por dia: "))

# leche = (k * x) / 7

# print("Los litros de leche producidos por semana en la granja son: %d" % leche)

################### 

# Dado un n ́umero entero, determinar si ese n ́umero corresponde al
# c ́odigo ASCII de una vocal min ́uscula. Ayuda: utilice la funci ́on
# chr(<n ́umero>) de Python que retorna el car ́acter ASCII
# correspondiente al n ́umero entero en el cual se eval ́ue la funci ́on.

# n = int(input("Ingrese un numero entero: "))

# correspone = chr(n)

# if correspone == "a" or correspone == "e" or correspone == "i" or correspone == "o" or correspone == "u":
#     print("El numero corresponde a una vocal minúscula")
# else:
#     print("El numero no corresponde a una vocal minúscula")

###############################################################################

# Dada una cadena de longitud 1, determine si el c ́odigo ASCII de
# primera letra de la cadena es par o no. Ayuda: utilice la funci ́on
# ord(<car ́acter>) de Python que retorna el c ́odigo ASCII de una
# cadena de longitud 1.

c = input("Ingrese una cadena de longitud 1: ")
c = ord(c)

if c % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

    