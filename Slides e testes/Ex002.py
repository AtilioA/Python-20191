# 3) Dados três números inteiros distintos, calcule o quadrado do sucessor do
# maior número.

def maior3(a, b, c):
    if (a >= b and b >= c):
        return a
    elif (b >= a and a >= c):
        return b
    else:
        return c

def quadradoSucessorMaior(a, b, c):
    maior = maior3(a, b, c)
    sucessorMaior = maior + 1
    return sucessorMaior ** 2
