# 12) Gere uma lista com a sequencia de fibonacci até um numero n.

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
