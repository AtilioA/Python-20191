# 6. Foram anotadas as idades e alturas dos alunos de uma turma e armazenados
# em uma lista cujos elementos são sublistas com dois elementos:
# o primeiro é a idade do aluno e o segundo a sua altura.
# Faça uma função que receba esta lista e, utilizando as funções abaixo,
# determine e mostre quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

# a) Faça a função MediaTurma (lista) que recebe a lista com
# com idade e altura de cada um dos alunos e retorna a média de altura da turma.
# b) Faça a função Conta_Baixinhos (lista, media), que recebe a lista com
# idade e altura de cada um dos alunos e a média de altura da turma,
# retornando quantos alunos com mais de 13 anos
# estão abaixo da média de altura da turma.

from functools import reduce


def get_idade(subAlunos):
    if not subAlunos:
        return subAlunos
    else:
        return subAlunos[0]


def get_altura(subAlunos):
    if not subAlunos:
        return subAlunos
    else:
        return subAlunos[-1]


def media_turma(lista):
    def soma_lista(lista):
        return reduce(lambda x, y: x + y, lista)

    alturas = map(get_altura, lista)
    nAlunos = len(lista)
    media = soma_lista(alturas) / nAlunos

    return media


alunos = [
    [1, 150], [10, 150], [21, 160], [34, 160],
    [21, 60], [11, 0], [4, 0], [100, 50]
]

print(media_turma(alunos))


def conta_baixinhos(lista, media):
    if not lista:
        return 0
    elif get_idade(lista[0]) < 13:
        return 0
    elif get_altura(lista[0]) < media:
        return 1 + conta_baixinhos(lista[1:], media)


print(conta_baixinhos(alunos, media_turma(alunos)))
