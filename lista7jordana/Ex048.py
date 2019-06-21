from math import sqrt
from functools import reduce

# a)


def maior_elemento(lista):
    def maior(a, b):
        if a > b:
            return a
        else:
            return b

    return reduce(maior, lista)


def menor_elemento(lista):
    def menor(a, b):
        if a < b:
            return a
        else:
            return b

    return reduce(menor, lista)


# b)
def soma_elementos(lista):
    def soma(a, b):
        return a + b

    try:
        if not lista:
            raise TypeError()
    except TypeError:
            pass

    return reduce(soma, lista)


# c)
def ocorrencias1(lista):
    return len(list(filter(lambda x: lista[0] == x, lista)))


# d)
def media_elementos(lista):
    return soma_elementos(lista) / len(lista)


# e)
def mais_prox_media(lista):
    media = media_elementos(lista)

    dist = map(abs, map(lambda x: x - media, lista))
    maisProx = menor_elemento(dist)

    return lista[dist.index(maisProx)]


# f)
def soma_negativos(lista):
    def negativo(a):
        return a < 0

    return soma_elementos(filter(negativo, lista))


# e)
def n_vizinhos_iguais(lista):
    # hmm
    return -1
