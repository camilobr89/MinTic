
"""
# Palabras reservadas para python:
and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

#Dictionary:
Su esructura de datos más común y más utilizada en Python. Se conforma por claves (keys) y valores (values).

Metodo update sirve para actualizar un diccionario con otro diccionario. o unir un diccionario con un diccionario.

Para eliminar una clave de un diccionario se utiliza (del diccionario[clave]).

Dict sirve para convertir una lista en un diccionario, para usar esta opcion es necesario que la lista este en pares.

json es un estandar para almecenar informacion en diccionarios

tipos de objetos de json:
object, arrery, string, number, boolean, null

tipos de objetos en python:
list, tuple, dict, set, str, int, float, bool, None

funciones incluidas son las siguientes:
len, pop, append, remove, insert, count, sort, reverse, min, max, sum, range, enumerate, sorted, reversed, map, filter, zip, reduce

funciones definidas por el usuarion son las siguientes:
abs, all, any, bin, bool, chr, classmethod, compile, complex, dir, divmod, enumerate, eval, exec, filter, format, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, isinstance, issubclass, iter, len, list, locals, map, max, min, next, object, oct, open, ord, pow, print, property, range, repr, reversed, round, set, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip

las funciones sin argumentos son las que no tienen un argumento, las funciones con argumentos son las que tienen un argumento.

"""

k = 5 
def func():
    global k
    k = k+7
    print(k)
    k = 10
func()
print(k)

