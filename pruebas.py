

contadorF = 0
contadorV = 0
x = ''

reloj = input("Ingrese las armas del reloj: ")

armasF = input("Ingrese las armas del equipo FIOTIA: ")
armasV = input("Ingrese las armas del equipo VIGBIANA: ")

i = 0

while i < len(reloj):
    if reloj[i] in armasF:
        contadorF += 1
    else:
        contadorF += 0
    if reloj[i] in armasV:
        contadorV += 1
    else:
        contadorV += 0
    i += 1
    if contadorF == contadorV:
        x = str("≈")
    elif contadorF > contadorV:
        x = str("V")
    else:
        x = str("F")
    
    print(x, end="")

    
    

    











