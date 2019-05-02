#  Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento da população de coelhos (1) através de uma seqüência de números naturais que passou a ser conhecida como seqüência de Fibonacci (2). O n-ésimo número da seqüência de Fibonacci Fn é dado pela seguinte fórmula de recorrência:
#           Faça um programa que, dado n, calcula Fn


def fibRecursivo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibRecursivo(n - 1) + fibRecursivo(n - 2)

def fibIterativo(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        aux = f2
        f2 = f1 + f2
        f1 = aux
    return f1
