"""

Considere dos equipos: VIGBIANA y FIOTIA. Solo un jugador de un determinado equipo se enfrenta a cualquier otro jugador del equipo contrario. Sin embargo, todas las armas están desalineadas, y lo único que se puede hacer es disparar hacia arriba con la esperanza de tener suerte para infligir daño al oponente.

Cada tipo de arma se representará con uno de los siguientes caracteres simétricos:

.

-

+

*

T

Y

|

W

X

M

 

Cada equipo elige sus posibles armas con las que atacar al equipo rival. El reloj de juego muestra el arma que va a tener efecto contra la otra en cada momento del juego. Si cualquier arma utilizada por los clanes golpea exactamente la representada por el reloj del juego, se anota un punto para ese equipo y se debe informar el progreso de la puntuación. Para representar el estado del juego en cada momento, se utiliza la siguiente convención: si VIGBIANA está ganando, se mostrará una 'V', si están empatadas un '≈' (ASCII 247 en UTF-8), y si están ganando el FIOTIA, se muestra una 'F'.

Desarrolla un programa que te permita recibir las letras que representan las armas elegidas por cada equipo, que reciba la información sobre las vulnerabilidades de las armas dadas por el reloj del juego, y que imprima el estado del juego en pantalla en cada momento de tiempo.

Ejemplos.

Entradas
+XMY*|

+XWY.-

WWX.-.+M-M|

|+..+XM|XM

Salida

FFFFFFFFFFFFFFFFFFFFF

"""



contadorF = 0
contadorV = 0
x = ''
armasF = input("Ingrese las armas del equipo FIOTIA: ")
armasV = input("Ingrese las armas del equipo VIGBIANA: ")
reloj = input("Ingrese las armas del reloj: ")

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
