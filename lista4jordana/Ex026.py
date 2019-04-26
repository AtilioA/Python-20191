# A força requerida para comprimir uma mola linear é dada pela equação F = k*x onde F é
# a força em N (Newton), x é a compressão da mola em m (metro), e k é a constante da
# mola em N/m (Newton por metro).
# A energia potencial armazenada na mola comprimida é dada pela
# equação E = 1/2 * k * x^2 onde E é a energia em J (joule).
#
# Defina funções para calcular a
# compressão e a energia potencial armazenada em uma mola, dadas a constante elástica
# da mola e a força usada para comprimi-la.


def compressaoMola(F, k):
    x = F / k
    return x

def compressaoMola2(l, l0):
    x = l - l0
    return x

def energiaPotencialMolaForca(F, k):
    x = compressaoMola2(F, k)
    E = (1 / 2) * k * x ** 2
    return E

def energiaPotencialMolaConstante(k, x):
    E = ((1 / 2) * k) * x ** 2
    return E
