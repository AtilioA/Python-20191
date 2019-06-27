# 12. Faça uma função que receba uma lista de números armazenados de forma crescente , e
# dois valores ( limite inferior e limite superior), e exiba a sublista cujos elementos são maiores
# ou iguais ao limite inferior e menores ou iguais ao limite superior


def intervalo(listaOrdenada, limInferior, limSuperior):
    if not listaOrdenada:
        return []
    elif listaOrdenada[0] >= limInferior and listaOrdenada[0] <= limSuperior:
        return [listaOrdenada[0]] + \
            intervalo(listaOrdenada[1:], limInferior, limSuperior)
    else:
        return intervalo(listaOrdenada[1:], limInferior, limSuperior)


lista = [1, 2, 3, 4, 5, 6, 7]
limInferior = 2
limSuperior = 5

print(intervalo(lista, limInferior, limSuperior))
