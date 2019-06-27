# 10. Faça uma função que:
# a. receba duas listas e exiba a união destas listas
# b. receba duas listas e exiba a interseção destas listas
# c. receba duas listas e exiba a intercalação destas listas, isto é, 1º da 1ª lista, 1º da 2ª lista,
# 2º da 1ª lista, 2º da 2ª lista.


def remove_duplicata(lista):
    if not lista:
        return lista
    elif lista[0] not in lista[1:]:
        return [lista[0]] + remove_duplicata(lista[1:])
    else:
        return remove_duplicata(lista[1:])


def mantem_duplicata(lista):
    if not lista:
        return lista
    elif lista[0] in lista[1:]:
        return [lista[0]] + mantem_duplicata(lista[1:])
    else:
        return mantem_duplicata(lista[1:])


def uniao(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    else:
        l3 = l1 + l2
        return remove_duplicata(l3)


def intersecao(l1, l2):
    if not l1 or not l2:
        return []
    else:
        l3 = l1 + l2
        return mantem_duplicata(l3)


def intercala(l1, l2):
    if not l1:
        return l1
    elif not l2:
        return l2
    else:
        return [l1[0]] + [l2[0]] + intercala(l1[1:], l2[1:])


l1 = [1, 4, 7]
l2 = [1, 7, 8, 10]

print(uniao(l1, l2))
print(intersecao(l1, l2))
print(intercala(l1, l2))
