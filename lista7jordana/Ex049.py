from math import *
from functools import *
from Ex046 import *

def éVogal(string):
    return string.lower() in "aeiou"

def vogais(strings):
    return list(map(éVogal, strings))

def maiorString(strings):
    def maiorLen(s1, s2):
        if len(s1) > len(s2):
            return s1
        else:
            return s2

    return reduce(maiorLen, strings)

def mediaVogais(strings):
    def tamanhoStrings(strings):
        tamanhos = map(len, strings)
        return somaElementos(tamanhos)

    return 0;
    # return len(list(filter(True, map(éVogal, strings)))) / tamanhoStrings(strings)

strings = ["321", "sim de fato", "setima lista de exercícios"]

print(list(map(vogais, strings)))

# def éVdd(booleano):
#     if booleano == True:
#         return True
#     else:
#         return False
# triste
