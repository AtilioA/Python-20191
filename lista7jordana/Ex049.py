# from math import sqrt
from functools import reduce
from Ex048 import soma_elementos

string = "sétima lista de exercícios"
strings = ["321", "sim de fato", "setima lista de exercícios"]


# a)
def maior_string(strings):
    def maior_len(s1, s2):
        if len(s1) > len(s2):
            return s1
        else:
            return s2

    return reduce(maior_len, strings)


# b)
def é_vogal(string):
    return string.lower() in "aâáãeêéiîíôoõuú"


def conta_vogais(string):
    return len(list(filter(é_vogal, string)))


def conta_vogais_strings(strings):
    return list(map(conta_vogais, strings))


def media_vogais(strings):
    try:
        if not strings:
            print("String vazia")
        else:
            totalVogais = soma_elementos(conta_vogais_strings(strings))
            totalElementos = soma_elementos(map(len, strings))
            media = totalVogais / totalElementos
            return media
    except ValueError:
        pass


# c)
def ocorrencias1(lista):
    return len(list(filter(lambda x: lista[0] == x, lista)))


# d)
def lex_maior(strings):
    try:
        if not strings:
            print("String vazia")
        else:
            return reduce(lambda x, y: maior(x, y), strings)
    except ValueError:
        pass


def maior(a, b):
    if a >= b:
        return a
    else:
        return b


print(lex_maior(strings))

print(conta_vogais(strings))
print(conta_vogais_strings(strings))
print(media_vogais(strings))

strings2 = ['eae', 'oi', 'opa', 'meu']
print(ocorrencias1(strings2))
