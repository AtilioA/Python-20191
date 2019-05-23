def somatorioLista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somatorioLista(lista[1:])


lista = [1, 2, 3]
print(somatorioLista(lista))
