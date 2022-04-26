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

#####
