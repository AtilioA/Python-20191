from functools import reduce

# a) Calcule termo de ordem n da sequência de fibonacci.


def fib_recursivo(n):
    if n < 2:
        return n
    else:
        return fib_recursivo(n - 1) + fib_recursivo(n - 2)


# b) Calcule o MDC de dois números naturais.
def mdc_recursivo(x, y):
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


def mod(x, y):
    if abs(x) > abs(y):
        return mod(abs(x) - abs(y), abs(y))
    elif abs(x) < abs(y):
        return abs(x)
    else:
        return 0


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
def é_par(n):
    return n % 2 == 0


def é_ímpar(n):
    return n % 2 != 0


def soma_par_sub_ímpar(lista):
    if lista == []:
        return 0
    elif é_par(lista[0]):
        return lista[0] + soma_par_sub_ímpar(lista[1:])
    elif é_ímpar(lista[0]):
        return -lista[0] + soma_par_sub_ímpar(lista[1:])


lista = [2, 5, 10]
# print(soma_par_sub_ímpar(lista))


# g) Dada uma lista ordenada, insira um elemento na ordem.
def insere_ordenado(n, listaOrdenada):
    if not listaOrdenada:
        return [n]
    elif listaOrdenada[0] > n:
        return [n] + listaOrdenada
    else:
        return [listaOrdenada[0]] + insere_ordenado(n, listaOrdenada[1:])


# h) Dada uma lista qualquer, ordene-a.
def insertion_sort(lista):
    if not lista:
        return lista
    else:
        return insere_ordenado(lista[0], insertion_sort(lista[1:]))

# listaOrdenada = [2, 5, 10]
# print(insere_ordenado(7, listaOrdenada))
# print(insertion_sort([1, 7, 3, 6, 5, 10]))


# i) Elimine os elementos repetidos de uma lista.
def remove_duplicata(lista):
    if not lista:
        return lista
    elif lista[0] not in lista[1:]:
        return [lista[0]] + remove_duplicata(lista[1:])
    else:
        return remove_duplicata(lista[1:])

# print(remove_duplicata([1, 5, 6, 10, 10, 10, 10, 8, 9, 5, 3]))


def remove_k_duplicata(k, lista):
    if not lista:
        return lista
    elif k not in lista[1:]:
        return [k] + remove_duplicata(lista[1:])
    else:
        return remove_duplicata(lista[1:])


# j) Calcule a quantidade de vezes que um elemento k ocorre em uma lista
def ocorrencias(k, lista):
    listaOcorrencias = [x for x in lista if x == k]
    return len(listaOcorrencias)

# print(ocorrencias(5, [1, 7, 5, 3, 5, 3, 7, 5, 7, 88, 6, 6, 5, 9]))


# k) Para cada elemento de uma lista, informe a quantidade de vezes
# que cada um deles ocorre numa lista. [(elemento, quantidade), ...]
def quantidade_vezes_elementos(lista):  # ???
    if not lista:
        return lista
    else:
        return [(lista[0], ocorrencias(lista[0], lista))]
        + quantidade_vezes_elementos(lista[1:])

# lista = [3, 2, 3, 1]
# print(ocorrencias(lista[0], lista))
# print(quantidade_vezes_elementos(lista))
# print(quantidade_vezes_elementos(lista[1:]))


# l) Ordene a lista anterior em ordem decrescente de ocorrência e valor.
# mas eu não tenho a lista anterior :O

# m) Dada uma lista e um número natural k, informe os elementos menores do que k.
def elementos_menores_k(k, lista):
    return [x for x in lista if x < k]


# print(elementos_menores_k(5, [1, 7, 3, 4, 8, 967]))


# n) Obtenha o maior e o menor elemento de uma lista
def maior_lista(lista):
    def maior(a, b):
        if a > b:
            return a
        else:
            return b
    if not lista:
        return lista
    else:
        return reduce(maior, lista)


def menor_lista(lista):
    def menor(a, b):
        if a < b:
            return a
        else:
            return b
    if not lista:
        return lista
    else:
        return reduce(menor, lista)

# lista = [1,57,8,4,2,5,-5,88,4]
# print(maior_lista(lista), menor_lista(lista))


# o) Obtenha uma lista com o quadrado dos números divisíveis por 3 de 1 a n.
def quadrado_divisiveis_3(n):
    intervalo = list(range(1, n + 1))
    divisiveis = [x for x in intervalo if x % 3 == 0]
    quadradoDivisiveis = list(map(lambda x: x**2, divisiveis))

    return quadradoDivisiveis

# print(quadrado_divisiveis_3(10))


# p) Obtenha uma lista com o resto da divisão por 3 dos números pares de 1 a n.
def resto_div3_pares(n):
    intervalo = list(range(2, n + 1, 2))
    restos = [x % 3 for x in intervalo]

    return restos

# print(resto_div3_pares(10))


# q) Dada uma lista, obtenha as duplas dos elementos consecutivos de ordem ímpar da lista.
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] => [(10, 8), (8, 6), (6, 4), (4, 2)]
# l = [10, 9, 8, 7, 5, 4, 3, 2, 1]a


# r) Dada uma lista, obtenha as triplas dos elementos consecutivos divisíveis por 3.
# range(1,20) => [(3, 6, 9), (6, 9, 12), (9, 12, 15), (12, 15, 18)]


# s) Calcule a multiplicação de dois números naturais usando apenas soma.
# def multiplicao_por_soma(n1, n2):


# t) Calcule a potência de x elevado a y usando apenas multiplicação.
# def potencia_por_multiplicacao(x, y):


# Dê duas soluções para a seguinte questão, seguindo os paradigmas aplicativo e
# recursivo:
# u) Verifique se todos os elementos de uma lista são distintos.
# v) Verifique se ao menos dois dos elementos de uma lista são iguais.
# w)


# def sao_todos_distintos_aplicativo(lista):
    # AAA
    # return not mantem_duplicata(lista)

# print(sao_todos_distintos_aplicativo([1,2,3,4,5,5]))


def mantem_duplicata(lista):
    if not lista:
        return lista
    elif lista[0] in lista[1:]:
        return [lista[0]] + mantem_duplicata(lista[1:])
    else:
        return mantem_duplicata(lista[1:])


def sao_todos_distintos_recursivo(lista):
    return not mantem_duplicata(lista)


print(sao_todos_distintos_recursivo([1, 2, 3, 4, 5, 5]))


def ao_menos_dois_iguais_recursivo(lista):
    if mantem_duplicata(lista):
        return True
    else:
        return False


print(ao_menos_dois_iguais_recursivo([1, 2, 3, 4, 5, 5]))

# x) Dadas duas listas de elementos distintos, determinar a união delas.
# Ex: [1,2,3,4] e [3,4,5,6] => [1,2,3,4,5,6]


def uniao(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    else:
        l3 = l1 + l2
        return remove_duplicata(l3)

# print(uniao([1, 2, 3, 4], [3, 4, 5, 6]))


# y) Dadas duas listas de elementos distintos, determinar a interseção delas.
def intersecao(l1, l2):
    if not l1 or not l2:
        return []
    else:
        l3 = l1 + l2
        return mantem_duplicata(l3)

# print(intersecao([1, 2, 3, 4], [3, 4, 5, 6]))
