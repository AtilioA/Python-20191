# 3) Dada uma lista l, contendo uma quantidade igual de números inteiros pares e ímpares (em
# qualquer ordem), defina uma função que, quando avaliada, produz uma lista na qual esses
# números pares e ímpares encontram-se alternados.

def éPar(n):
    return n % 2 == 0

def éÍmpar(n):
    return n % 2 != 0

def listaPar(lista):
    return list(filter(éPar, lista))

def listaÍmpar(lista):
    return list(filter(éÍmpar, lista))

def juntaParImpar(lista):
    lPar = listaPar(lista)
    lÍmpar = listaÍmpar(lista)
    return list(zip(lPar, lÍmpar))

lista = [5,6,7,3,6,2,5,4]
print(juntaParImpar(lista))
