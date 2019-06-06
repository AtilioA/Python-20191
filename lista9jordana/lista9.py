# a) Calcule termo de ordem n da sequência de fibonacci.
def fibRecursivo(n):
    if n < 2:
        return n
    else:
        return fibRecursivo(n - 1) + fibRecursivo(n - 2)

# b) Calcule o MDC de dois números naturais.
def mdcRecursivo(x, y):
    if x == y:
        return x
    elif x > y:
        return mdcRecursivo(x - y, y)
    else:
        return mdcRecursivo(y, x)

# c) Calcule o quociente (div) e o resto (mod) da divisão inteira e entre dois números naturais
def div(x, y):
    if abs(x) > abs(y):
        return 1 + div(abs(x) - abs(y), abs(y))
    elif abs(x) < abs(y):
        return 0
    else:
        return 1

# d) Calcule o somatório dos elementos de uma lista.
def somatorio(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + somatorio(lista[1:])

# e) Calcule o produto dos elementos de uma lista.
def produtorio(lista):
    if lista == []:
        return 1
    else:
        return lista[0] * produtorio(lista[1:])

# lista = [2, 5, 10]
# print(produtorio(lista))

# f) Some os elementos pares e subtraia os impares de uma lista.
def éPar(n):
    return n % 2 == 0
def éÍmpar(n):
    return n % 2 != 0

def somaParSubÍmpar(lista):
    if lista == []:
        return 0
    elif éPar(lista[0]):
        return lista[0] + somaParSubÍmpar(lista[1:])
    elif éÍmpar(lista[0]):
        return -lista[0] + somaParSubÍmpar(lista[1:])

lista = [2, 5, 10]
# print(somaParSubÍmpar(lista))

# g) Dada uma lista ordenada, insira um elemento na ordem.
def insereOrdenado(n, listaOrdenada):
    if lista == []:
        return lista + [n]
    elif lista[0] < n:
        return insereOrdenado(n, listaOrdenada[1:])
    else:
        return [n] + listaOrdenada

listaVazia = [4,8,20]
# print(insereOrdenado(7, listaVazia))
