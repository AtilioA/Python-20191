# Find the sum of all the multiples of 3 or 5 below 1000.

def div3E5(n):
    somaMultiplos = 0

    for i in range(0, n):
        if (i % 3 == 0 or i % 5 == 0):
            somaMultiplos += i
    return somaMultiplos

n = 1000
print(div3E5(n))
