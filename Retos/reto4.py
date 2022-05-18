"""
Gi, Ale y Nico están coleccionando las láminas del Mundial 2024 de  Pannini Paganini y encontraron una tienda OnLine donde vende algunas láminas, cada lámina es vendida a un cierto precio. Como ellos tienen una lista con los códigos de las láminas que les hacen falta, quieren saber los códigos de las láminas que pueden comprar y el precio a pagar por dicha compra. Realizar un programa que dado un diccionario (en formato JSON) que tiene las parejas código:precio de todas las láminas que tiene la tienda, y que dada la lista de códigos de láminas que les faltan a Gi, Ale y Nico (separados por espacios), imprima el precio de las láminas que pueden comprar y los códigos  de las láminas que pueden comprar:

ejemplo:

Entrada:
{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}
d p h u i e t q

Salida:
290
d u t q
"""

import json


dict = json.loads(input())
codigos = input().split()
suma = 0
for i in codigos:
    if i in dict:
        suma += dict[i]       
print(suma)

for i in codigos:
    if i in dict:
        print(i, end=" ")






