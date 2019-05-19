# 9) Defina uma função que ordene uma lista de forma crescente.

def permuta(lista, i1, i2):
    aux = lista[i1]
    lista[i1] = lista[i2]
    lista[i2] = aux
    return lista

def bolhaSorte(lista):
    for i, x in enumerate(lista):
        if (i + 1) < len(lista):
            if lista[i + 1] < x:
                permuta(lista, i, i + 1)
                bolhaSorte(lista)
    return lista
