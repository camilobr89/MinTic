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

cx = float(input("Ingrese la coordenada en X del centro del circulo: "))
cy = float(input("Ingrese la coordenada en y del centro del circulo: "))
r = float(input("Ingrese el radio del circulo: "))


def circulo(cx,cy,r):
    x = float(input("Ingrese el punto x: "))
    y = float(input("Ingrese el punto y: "))

    if (x - cx)*2 + (y - cy)**2 <= r*2:
        return "El punto esta dentro del circulo"
    else:
        return"El punto esta fuera del circulo"
    
print(circulo(cx,cy,r))

###############################################################################

# Ejercicio 3

# Mi mam ́a me manda a comprar P panes a $ 300 cada uno, M bolsas
# de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
# programa que me diga las vueltas (o lo que quedo debiendo) cuando
# me da un billete de B pesos.

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