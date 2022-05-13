"""
PROMUSIC se ha enterado de su capacidad auditiva, su contexto melómano y sus habilidades en desarrollo de software. Por estas tres características, que son muy difíciles de encontrar, lo han contactado para que genere alguna idea innovadora que permita realizar el lanzamiento de ONLY MUSIC.

La dinámica de ONLY MUSIC consiste en hacer sonar una serie de cuerdas, una cuerda a la vez, y cada cuerda asociada a una letra distinta del alfabeto; lamentablemente, el sonido algunas veces no suena con calidad perfecta, así que el sonido de la cuerda puede llegar representado por la letra del alfabeto en minúscula o en mayúscula. La idea es que luego de escuchar la sucesión de sonidos, se pueda determinar,  cuál cuerda sonó y cuántas veces sonó la misma cuerda de manera consecutiva.

Un ejemplo sencillo de ésta dinámica se puede hacer con la canción “SON PARA UN SONERO”, que inicia con la secuencia: E,E,e,E,E,d,EE,D,c,C. En este caso, los sonidos generados serán E (con cinco repeticiones), D (con una repetición), E (con dos repeticiones), D (con una repetición), y C (con dos repeticiones).

Realizando el análisis completo usted decide construir un programa que resuelve la propuesta realizada.

Inicialmente el programa recibe la sucesión de cuerdas que está escuchando, que puede estar en minúscula o en mayúscula, y cada sonido separado por coma.

La salida estará representada por una sucesión de cuerdas, representadas en mayúscula, sin tener en cuenta los sonidos repetidos, y debajo de cada cuerda, la cantidad de veces que sonó esta de manera consecutiva.

Entrada

La entrada consta de una sucesión de caracteres separados por coma que corresponden a las cuerdas asociadas a los sonidos determinados.

Salida

La salida consta de dos líneas: la primera es la sucesión de sonidos de cuerdas sin repeticiones, en mayúscula y separadas por espacio; la segunda es la cantidad de veces que se repitió cada sonido de cuerda de manera consecutiva, separado también por espacio.

ejemplo:

entrada:
e,E,c,E,b,d,f,F,c,e,a,c,a,c,e

salida:
E C E B D F C E A C A C E
2 1 1 1 1 2 1 1 1 1 1 1 1

"""



# from itertools import groupby
# notas = tuple(map(str.upper, input().split(',')))
# for i, x in groupby(notas):
#     print(i, end=" ")
# print()
# for i, x in groupby(notas):
#     print(len(list(x)), end=" ")
# print()

#######################################################################################################################

# from itertools import groupby

# r=input().split(",")
# mayuscula=list(map(lambda x:x.upper(),r))

# c= groupby(list(mayuscula))
# for k,g in groupby(mayuscula):
#     print(k,end=" ")
# print()
# for k,g in c:
#     print(len(list(g)),end=" ")
# print()

#######################################################################################################################














