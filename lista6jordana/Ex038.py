# 4) Dada uma lista xs, fornecer uma tupla contendo o menor e o maior elemento dessa lista.

from functools import *

def minN(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2

def minLista(lista):
    return reduce(minN, lista)

def maxN(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def maxLista(lista):
    return reduce(maxN, lista)

def tuplaMenorMaiorLista(lista):
    return (minLista(lista), maxLista(lista))

lista = [5,6,7,3,6,2,5,4]
print(tuplaMenorMaiorLista(lista))
