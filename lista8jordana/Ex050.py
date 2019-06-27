# Dada uma lista de listas, ordene a lista de acordo com o tamanho das sublistas.

l = [[2, 3, 4], [2], [5, 7, 9, 9, 6, 2, 1], [2, 2]]


def tamanhoSublista(lista):
    return list(map(len, lista))


def insere_ordenado(n, listaOrdenada):
    if not listaOrdenada:
        return [n]
    elif listaOrdenada[0] > n:
        return [n] + listaOrdenada
    else:
        return [listaOrdenada[0]] + insere_ordenado(n, listaOrdenada[1:])


# h) Dada uma lista qualquer, ordene-a.
def insertion_sort_tam(lista):
    if not lista:
        return lista
    else:
        return insere_ordenado(lista[0], insertion_sort_tam(lista[1:]))

print(tamanhoSublistas(l))
