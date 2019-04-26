import math as jordana

def cosAlpha(a, b, c):
    cos = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    return cos

def senAlpha(cosAlpha):
    sen = jordana.sqrt(1 - cosAlpha ** 2)
    return sen

def calculaH(b, senAlpha):
    h = b * senAlpha
    return h


def areaTriangulo(a, b, c):
    h = calculaH(b, senAlpha(cosAlpha(a, b, c)))
    A = (c * h) / 2
    return round(A, 5)
