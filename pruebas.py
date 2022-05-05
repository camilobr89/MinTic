"""

# Earth sixty nine.

# Earth sixty nine, is a video game developed by BII (Business Intelligence Innovation), which includes a modality called Total Simulation, in which users are randomly assigned to one of two teams and they must fight all of the other team until the allotted time is up.

# You are applying to work for BII and in the interview you are asked to develop a characteristic that consists of the following:

# Consider two teams: VIGBIANA and FIOTIA. Only one player from a certain team is matched against any other player from the opposing team. However, all the weapons are misaligned, and the only thing to do is shoot upwards hoping to get lucky to inflict damage on the opponent.

# Each type of weapon will be represented with one of the following symmetrical characters:

#   .

#   -

#   +

#   *

#   T

#   Y

#   |

#   W

#   X

#   M

 

# Each team chooses its possible weapons with which to attack the rival team. The game clock displays the weapon that is going to have an effect against the other at each moment of the game. If any weapon used by clans hits the exact one represented by the game clock, a point is scored for that team and scoring progress must be reported. To represent the state of the game at all times, the following convention is used: if VIGBIANA is winning, a 'V' will be displayed, if they are tied a '≈' (ASCII 247 in UTF-8), and if they are winning the FIOTIA, an 'F' is shown.

# Develop a program that allows you to receive the letters that represent the weapons chosen by each team, that receives the information on the vulnerabilities to the weapons given by the game clock, and that prints the state of the game on the screen at each moment of time.

# """

# armas = ['.', '-', '+', '*', 'T', 'Y', '|', 'W', 'X', 'M']

# myArmas = iter(armas)

# armasv = input("Ingrese las armas del equipo VIGBIANA: ")
# armasf = input("Ingrese las armas del equipo FIOTIA: ")
# vulnev = input("Ingrese las armas vulnerables del equipo VIGBIANA: ")
# vulnef = input("Ingrese las armas vulnerables del equipo FIOTIA: ")

# while True:
#     try:
#         print(next(myArmas))
#     except StopIteration:
#         break
# for i in range(len(armasv)):
#     if armasv[i] == armasf[i]:
#         print('=')
#     elif armasv[i] == ".":
#         print('V')
#     else:
#         print('F')

#############

# Desarrollar un programa que imprima el cuadrado del numero que el
# usuario ingresa mientras que el numero ingresado no sea negativo.

numero = int(input("ingrese el numero: "))
while numero > 0:
    potencia = numero ** 2
    print("El cuadrado del numero es: %d" %potencia)
    break


