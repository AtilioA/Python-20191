# 1) Dada uma lista, determine o seu maior elemento.

from functools import *

def minN(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

def minLista(lista):
    return reduce(minN, lista)
