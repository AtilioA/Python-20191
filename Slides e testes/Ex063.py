# def tupla1(tupla):
#     return tupla[0]


# def mantem_duplicata(lista):
#     if not lista:
#         return lista
#     elif tupla1(lista[1]) in (lista[1])[1:]:
#         return [lista[1]] + mantem_duplicata(lista[1:])
#     else:
#         return mantem_duplicata(lista[1:])


# def conta_rep(historico):
#     materiasRepetidas = mantem_duplicata(historico)


# historico = [2018102974, [(100, (2018, 1), 10), (101, (2018, 1), 10),
#                           (150, (2018, 1), 10), (170, (2018, 1), 10)]]
# conta_rep(historico)

def merge_ordenado(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1[0] < l2[0]:
        return [l1[0]] + merge_ordenado(l1[1:], l2)
    else:
        return [l2[0]] + merge_ordenado(l1, l2[1:])


l1 = [1, 2, 3, 4, 5]
l2 = [2, 6, 8, 10]


def merge_sort(lista):
    if len(lista) < 2:
        return lista
    else:
        metade = len(lista) // 2
        return merge_ordenado(merge_sort(lista[:metade]), merge_sort(lista[metade:]))


lista = [5, 9, 3, 1, 5, 7, 8, 3]
print(sorted(lista))
print(merge_sort(lista))
