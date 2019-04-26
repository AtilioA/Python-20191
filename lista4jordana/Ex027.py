# Defina uma função que receba a indutância L e a capacitância C, e resulta na frequência
# de ressonância de um aparelho de rádio, dado que a fórmula da frequência é:
# f0 = 1 / (2 * pi * sqrt(L * C))

import math as jordana

def frequenciaDeRessonancia(L, C):
    f0 = 1 / (2 * jordana.pi * jordana.sqrt(L * C))
    return f0
