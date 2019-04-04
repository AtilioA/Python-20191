def quadrante(x, y):
    if (x > 0 and y > 0):
        return 1
    elif (x < 0 and y > 0):
        return 2
    elif (x < 0 and y < 0):
        return 3
    elif (x > 0 and y < 0):
        return 4
    elif (x == 0 and y < 0):
        return 'y-'
    elif (x == 0 and y > 0):
        return 'y+'
    elif (x > 0 and y == 0):
        return 'x-'
    elif (x < 0 and y == 0):
        return 'x+'
    else:
        return 0

def quadrantesRetangulo(x1, y1, x2, y2):
    quadP1 = quadrante(x1, y1)
    quadP2 = quadrante(x2, y2)

    if quadP1 == 0 and quadP2 != 0:
        return 1

    elif quadP1 == 1 and quadP2 == 1:
        return 1
    elif quadP1 == 1 and quadP2 == 2:
        return 2

    elif quadP1 == 2 and quadP2 == 2:
        return 1
    elif quadP1 == 2 and quadP2 == 3:
        return 2
    elif quadP1 == 2 and quadP2 == 4:
        return 4

    elif quadP1 == 3 and quadP2 == 3:
        return 1
    elif quadP1 == 3 and quadP2 == 4:
        return 2

    elif quadP1 == 'x+' and quadP2 == 4:
        return 1
    elif quadP1 == 'x-' and quadP2 == 3:
        return 1
    elif quadP1 == 'x-' and quadP2 == 4:
        return 2

    elif quadP1 == 'y+' and quadP2 == 4:
        return 2
    elif quadP1 == 'y-' and quadP2 == 1:
        return 1

    else:
        print('NAO SEI')

# print(quadrantesRetangulo(1, 1, 2, 2))
# print(quadrantesRetangulo(-1, 1, 2, -2))
# print(quadrantesRetangulo(-1, 1, -2, -2))
