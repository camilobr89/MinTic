def run():
    PANES = 300
    LECHE = 3300
    HUEVOS = 350

    b = int(input("Ingrese el valor del billete: "))
    p = int(input("Ingrese la cantidad de panes: "))
    l = int(input("Ingrese la cantidad de leche: "))
    h = int(input("Ingrese la cantidad de huevos: "))

    total_vueltas = b - (p * PANES + l * LECHE + h * HUEVOS)
 
    total_deuda = b - (p * PANES + l * LECHE + h * HUEVOS)
    
    if total_deuda < 0:
        # print("Usted debe devolver : " + "$" + str(abs(total_deuda)) + " pesos")
        print("Usted debe devolver $%d pesos" % abs(total_deuda))
    else:
        print("Sus vueltas son: $%d pesos" % total_vueltas)
        # print("Sus vueltas son: " +  "$" + str(total_vueltas), "pesos")

if __name__ == "__main__":
    run()