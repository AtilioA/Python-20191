import math

def pertenceIntervalo(x, a, b):
    if a > b:
        aux = a
        a = b
        b = aux

    if x >= a and x <= b:
        return True
    else:
        return False

# print(pertenceIntervalo(1, 2, 3))
# print(pertenceIntervalo(50, 3, 99))
# print(pertenceIntervalo(50, 99, 3))
# print(pertenceIntervalo(1, 3, 2))
# print(pertenceIntervalo(0, 0, 0))
# print(pertenceIntervalo(1, 0, 0))
