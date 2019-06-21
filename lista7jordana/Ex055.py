# Faça um programa que percorre uma lista com o seguinte formato:
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
# e imprima na tela algumas# informações.
# Essa lista indica o número de faltas que cada time fez em cada jogo.
# Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.

# O programa deve imprimir na tela:
# a) o total de faltas do campeonato
# b) o time que fez mais faltas
# c) o time que fez menos faltas

from Ex048 import soma_elementos

listaFaltas = [
    ['Brasil', 'Italia', [10, 9]],
    ['Brasil', 'Espanha', [5, 7]],
    ['Italia', 'Espanha', [7, 8]]
]


# pega lista de times
# pra cada partida, ve se cada time está nela
# pra cada time que estiver, pegar indice dele
# acessar lista de faltas com o indice do time
# somar e repetir


# a)
def total_faltas(listaFaltas):
    def terceiro(lista3):
        return lista3[2]

    faltas = list(map(terceiro, listaFaltas))
    totalFaltas = soma_elementos(map(soma_elementos, faltas))
    return totalFaltas


# b)
def remove_duplicata(lista):
    if len(lista) < 2:
        return lista
    elif lista[0] not in lista[1:]:  # O elemento é único, podemos adicioná-lo na lista final
        return [lista[0]] + remove_duplicata(lista[1:])
    else:  # O elemento não é único, não o adicionamos ainda
        return remove_duplicata(lista[1:])


def times_campeonato(listaFaltas):
    def primeiro(lista):
        if not lista:
            return lista
        else:
            return lista[0]

    def segundo(lista):
        if len(lista) < 2:
            return None
        else:
            return lista[1]

    timesRepetidos = list(map(primeiro, listaFaltas)) + list(map(segundo, listaFaltas))
    times = remove_duplicata(timesRepetidos)

    return times

print(f"Total de faltas do campeonato: {total_faltas(listaFaltas)}")
print(f"Time que fez mais faltas: {total_faltas(listaFaltas)}")
print(f"Time que fez menos faltas: {total_faltas(listaFaltas)}")

print(times_campeonato(listaFaltas))


def faltas_times(listaFaltas, times):
    print("\n", times)
    print(listaFaltas[0])
    return list(filter(lambda x: x in listaFaltas[0], times))

print(faltas_times(listaFaltas, times_campeonato(listaFaltas)))
