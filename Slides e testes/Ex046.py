def menorLista(lista):
    if len(lista) == 1:
        return lista[0]
    elif lista[0] < menorLista(lista[1:]):
        return lista[0]
    else:
        return menorLista(lista[1:])


lista = [55,78,2,8,0,2,8]
print(menorLista(lista))
