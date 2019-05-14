# 7) Defina uma função que avalia se, em uma dada lista de números, pelo menos um deles é par.

def éPar(n):
    return n % 2 == 0

def paresEmListaBool(lista):
    return map(éPar, lista)

def parEmLista(lista):
    return True in paresEmListaBool(lista)

lista = [5,6,7,3,5,4]
print(parEmLista(lista))
