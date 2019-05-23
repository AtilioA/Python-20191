from math import *
from functools import *

def maiorElemento(lista):
    def maior(a, b):
        if a > b:
            return a
        else:
            return b

    return reduce(maior,lista)

def menorElemento(lista):
    def menor(a, b):
        if a < b:
            return a
        else:
            return b

    return reduce(menor,lista)

def somaElementos(lista):
    def soma(a, b):
        return a + b

    return reduce(soma, lista)

def ocorrencias1(lista):
    return len(list(filter(lambda x: lista[0] == x, lista)))

def mediaElementos(lista):
    return somaElementos(lista) / len(lista)

def maisProxMedia(lista):
    media = mediaElementos(lista)

    dist = map(abs, map(lambda x: x - media, lista))
    maisProx = menorElemento(dist)

    return lista[dist.index(maisProx)]

def somaNegativos(lista):
    def negativo(a):
        return a < 0

    return somaElementos(filter(negativo, lista))

def nVizinhosIguais(lista):
    # hmm
    return -1
