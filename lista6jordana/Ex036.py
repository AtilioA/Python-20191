# 2) Dada uma lista, verifique se ela é não decrescente.

from functools import *

def minAB(a, b):
    return a > b

def listaDecrescente(lista):
    listaBool = reduce(minAB, lista)
    return True in listaBool

lista = [3,2,1]
print(listaDecrescente(lista))
