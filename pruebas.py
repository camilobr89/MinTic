def deuda(b, p, l, h):
    PANES = 300
    LECHE = 3300
    HUEVOS = 350

    return b - (p * PANES + l * LECHE + h * HUEVOS)

def run():
    b = int(input("Ingrese el valor del billete: "+ "$"))
    p = int(input("Ingrese la cantidad de panes: "))
    l = int(input("Ingrese la cantidad de leche: "))
    h = int(input("Ingrese la cantidad de huevos: "))

    if deuda(b, p, l, h) < 0:
        print("Usted debe devolver $%d pesos" % abs(deuda(b, p, l, h)))
    else:
        print("Sus vueltas son: $%d pesos" % deuda(b, p, l, h))

if __name__ == "__main__":
    run()