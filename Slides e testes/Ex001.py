# 2) Dados três comprimentos de lados l1, l2 e l3, verifique se podem formar
# um triângulo.

def formaTriangulo(l1, l2, l3):
    if((abs(l2 - l3) < l1 < l2 + l3) and
    (abs(l1 - l3) < l2 < l1 + l3) and
    (abs(l1 - l2) < l3 < l1 + l2)):
        print("Sim")
        return True
    else:
        print("Nao")
        return False

l1 = int(input("l1: "))
l2 = int(input("l2: "))
l3 = int(input("l3: "))
formaTriangulo(l1, l2, l3)
