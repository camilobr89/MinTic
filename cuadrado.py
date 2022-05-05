# Desarrollar un programa que imprima el cuadrado del numero que el
# usuario ingresa mientras que el numero ingresado no sea negativo.

numero = int(input("ingrese el numero: "))
while numero > 0:
    potencia = numero ** 2
    print("El cuadrado del numero es: %d" %potencia)
    break
