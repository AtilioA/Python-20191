from functools import *

# a)
def somaSituacao(dupla, y):
    return dupla[1] + y

def totalOcup(plateia):
    def soma(a, b):
        return a + b
    return reduce(soma, list(map(lambda x: x[1], plateia)))

plateia = [(1,0), (2,1), (3,0), (4,1), (5,1), (6,1)]
print(totalOcup(plateia))
