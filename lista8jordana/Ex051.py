# Dada uma lista de duplas formadas por nomes de alunos e suas respectivas médias de
# notas obtidas ao longo do curso, obter uma nova lista de duplas, ordenadas em ordem
# decrescente dessas médias.

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

def 
