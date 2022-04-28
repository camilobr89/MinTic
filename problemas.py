# 1. Ejercicio 1

# Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triangulo.
# Teorema de Pitágoras H2 = A2 + B2
# lado a, lado b y lado c

#si a < (b + c)
#si b < (a + c)
#si c < (a + b)


longitud_a = int(input("Introducir longitud a: "))
longitud_b = int(input("Introducir longitud b: "))
longitud_c = int(input("Introducir longitud c: "))

print(longitud_a,longitud_b,longitud_c)

if longitud_a <(longitud_b + longitud_c):
  print("es un triangulo")

elif longitud_b <(longitud_a + longitud_c):
  print("es un triangulo")

elif longitud_c <(longitud_a + longitud_b):
  print("es un triangulo")

else:
  print("no es un triangulo")

###############################################################################

# Ejercicio 2
# Dado el centro y el radio de un circulo, determinar si un punto de R2 pertenece o no al interior del circulo.

cx = float(input("Ingrese la coordenada en X del centro del cırculo: "))
cy = float(input("Ingrese la coordenada en y del centro del cırculo: "))
r = float(input("Ingrese el radio del cırculo: "))


def circulo(cx,cy,r):
    x = float(input("Ingrese el punto x: "))
    y = float(input("Ingrese el punto y: "))

    if (x - cx)*2 + (y - cy)**2 <= r*2:
        return "El punto esta dentro del cırculo"
    else:
        return"El punto esta fuera del cırculo"
    
print(circulo(cx,cy,r))