
# Desarrollar un algoritmo que reciba dos cadenas de caracteres y
# determine si la primera est ́a incluida en la segunda. Se dice que una
# cadena est ́a incluida en otra, si todos los caracteres (con repeticiones)
# de la cadena est ́a en la segunda cadena sin tener en cuenta el orden
# de los caracteres.

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

while len(cadena1) > 0 and len(cadena2) > 0:
    if cadena1 in cadena2:
        print("La cadena %s esta incluida en la cadena %s" %(cadena1, cadena2))
        break
    else:
        print("La cadena %s no esta incluida en la cadena %s" %(cadena1, cadena2))
        break