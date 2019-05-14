# 10) Dadas duas listas xs e ys, verificar se xs é sublista de ys.

def sublista(l1, l2):
    for x in l1:
        if x in l2:
            continue
        else:
            return False
    return True

l3 = [1,2,3,5,6,7]
l4 = [3,5,6]

print(sublista(l4, l3))
