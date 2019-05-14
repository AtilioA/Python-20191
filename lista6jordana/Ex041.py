# 8) Defina uma função que, dado um valor e uma lista, insira esse valor de forma ordenada na
# lista.

def ehMaior(a, b):
    return a > b

def ehMenor(a, b):
    return a < b

def insereOrdenado(x, lista):
    lMenorX = list(filter(lambda y: y < x, lista))
    lMaiorX = list(filter(lambda y: y > x, lista))
    lInserida = lMenorX + [x] + lMaiorX
    return lInserida


l = [1, 3, 4]
x = 2
print(insereOrdenado(x, l))
