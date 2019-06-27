# 8. Faça uma função que receba uma lista qualquer e retorne True se ela está ordenada ou
# False, caso contrário. Lembre-se que não é possível comparar elementos de tipos distintos.
# Caso o elemento seja uma sublista, a sublista deve ser verificada.


def esta_ordenada(lista):
    if not lista:
        return True
    elif len(lista) > 1 and lista[0] < lista[1]:
        return True and esta_ordenada(lista[1:])
    elif len(lista) == 1:
        return True
    else:
        return False


print(esta_ordenada([1, 5, 3]))
print(esta_ordenada([3, 2, 1]))
print(esta_ordenada([3, 2, 2]))

print(esta_ordenada([3, 5, 7, 5]))
print(esta_ordenada([3, 5, 7, 9]))
print(esta_ordenada([3, 3, 3, 3]))

print(esta_ordenada([3]))
print(esta_ordenada([]))

print(esta_ordenada([[2, 9], [3, 3], [5]]))
print(esta_ordenada([[2, 9], [3, 3], [1]]))
