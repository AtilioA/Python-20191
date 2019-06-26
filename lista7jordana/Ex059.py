# 9. Faça uma função que receba uma lista lNumeros e um valor,
# exiba a posição da 1ª ocorrência de valor em l.
# Caso o valor não pertença à lista, a função deve retornar -1
# e caso a lista esteja vazia, a função deve retornar -2


def posicao(lNumeros, valor):
    if not lNumeros:
        return -2
    elif valor not in lNumeros:
        return -1
    else:
        return lNumeros.index(valor) # eu sou pilantra

# print(posicao([2,6,7,8,5,6,3,2,6,5,4], 6))
