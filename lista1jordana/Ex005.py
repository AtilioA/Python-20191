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

# quadrante(0, 0)
# quadrante(0, 1)
# quadrante(1, 0)
# quadrante(1, 1)
# quadrante(1, -1)
# quadrante(-1, 1)
# quadrante(-1, -1)
