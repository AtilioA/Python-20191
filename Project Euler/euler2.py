# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def somafibonacciPar():
    somaTermos = 0
    anterior = 0
    atual = 1
    limite = 4000000

    while (atual <= limite):
        if (atual % 2 == 0):
            somaTermos += atual

        aux = atual
        atual = anterior + atual
        anterior = aux

    return somaTermos

print(f"\nSoma dos termos pares menores que 4,000,000 da sequência de Fibonacci: {fibonacciPar()}\n")
