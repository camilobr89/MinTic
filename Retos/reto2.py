
# Earth sixty nine.

# Earth sixty nine, es un videojuego desarrollado por BII (Business Intelligence Innovation), el cual Incluye una modalidad denominada Total Simulation, en la que los usuarios se asignan aleatoriamente a uno de dos equipos y estos deben combatir a todos los del otro equipo hasta que se termina el tiempo asignado. 

# Usted se está postulando para trabajar para BII y en la entrevista le piden que desarrolle una característica que consiste en lo siguiente:

# Considere dos equipos: VIGBIANA y FIOTIA. Solamente un jugador de determinado equipo se enfrenta contra cualquier otro jugador del equipo contrario. Sin embargo, todas las armas están desalineadas, y lo único que se puede hacer es disparar hacia arriba esperando contar con suerte para infligir daño sobre el rival. 

# Cada tipo de arma se va a representar con uno de los siguientes caracteres simétricos: 

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

 

# Cada equipo escoge sus posibles armas con las que se atacará al equipo rival. El reloj del juego despliega el arma que sí va a tener efecto contra el otro en cada momento del juego. Si algún arma usada por los clanes atina exactamente con la que representa el reloj del juego, se anota un punto a dicho equipo y se debe informar el progreso de la puntuación. Para representar el estado de la partida en cada momento se usa la siguiente convención: si VIGBIANA va ganando, se va a mostrar un 'V', si van empatados un '≈' (ASCII 247 en UTF-8), y si va ganando el FIOTIA, se muestra una 'F'. 

# Desarrolle un programa que permita recibir las letras que representan las armas elegidas por cada equipo, que reciba la información de las vulnerabilidades a las armas dadas por el reloj del juego, y que imprima en pantalla el estado del juego en cada momento del tiempoz

# armasV = input("Ingrese las armas del equipo VIGBIANA: ")
# armasF = input("Ingrese las armas del equipo FIOTIA: ")

# def juego(armasv, armasf, tiempo):
#     if armasv[tiempo] == armasf[tiempo]:
#         return "="
#     elif armasv[tiempo] == ".":
#         return "V"
#     else:
#         return "F"
    
# print(juego(armasV, armasF, 0))





# def juego(armasv, armasf, timpo):
#     resultados = ''

#     x = int(input("Ingrese el tiempo: "))

#     while x < timpo:
#         armasV = input("Ingrese las armas del equipo VIGBIANA: ")
#         armasF = input("Ingrese las armas del equipo FIOTIA: ")
#         for i in range(len(armasv)):
#             if armasv[i] == armasf[i]:
#                 resultados += '='
#             elif armasv[i] == ".":
#                 resultados += 'V'
#             else:
#                 resultados += 'F'
#         x += 1
#     return resultados

#     print(juego(armasV, armasF, timpo))

# if __name__ == "__main__":
#     juego()


###############################################################################

# def juego(armasv, armasf, tiempo):
#     ARMAS = ('.', '-', '+', '*', 'T', 'Y', '|', 'W', 'X', 'M')
#     resultados = ''
#     resultadosTotal = ''
#     for i in range(tiempo):
#         if armasv[i] == armasf[i]:
#             resultados += '='
#         elif armasv[i] == ".":
#             resultados += 'V'
#         else:
#             resultados += 'F'
#         resultadosTotal += resultados
#     return resultadosTotal
    

    

# def run():
#     tiempo  = int(input("Ingrese el tiempo: "))

#     i = 0

#     while i < tiempo:
#         armasV = input("Ingrese las armas del equipo VIGBIANA: ")
#         armasF = input("Ingrese las armas del equipo FIOTIA: ")
#         i += 1
#         print(juego(armasV, armasF, tiempo))
    
        

# if __name__ == "__main__":
#     run()






from mimetypes import init

def juego(armasv, armasf, vulnerabilidadesV, vulnerabilidadesF, tiempo):
    
    for i in range(len(armasv)):
        if armasv[i] == armasf[i]:
            resultados += '='
        elif armasv[i] == ".":
            resultados += 'V'
        else:
            resultados += 'F'
    return resultados




def run():
    tiempo = init(input("Ingrese el tiempo: "))
    i = 0
    while i < tiempo:
        
        armasV = input("Ingrese las armas del equipo VIGBIANA: ")
        armasF = input("Ingrese las armas del equipo FIOTIA: ")
        vulnerabilidadesV = input("Ingrese las vulnerabilidades del equipo VIGBIANA: ")
        vulnerabilidadesF = input("Ingrese las vulnerabilidades del equipo FIOTIA: ")
        i += 1
        print(juego(armasV, armasF, vulnerabilidadesV, vulnerabilidadesF, tiempo))

if __name__ == "__main__":
    run()
