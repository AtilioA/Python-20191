# 4) Dado um ponto P(x,y) do plano cartesiano, defina funções que descrevam a sua
# pertinência num losango, com os seus eixos paralelos aos eixos cartesianos, dado pelas
# coordenadas do vértice esquerdo e do vértice superior, como mostrado na figura.

def coefReta(x, y, x0, y0):
    m = (y - y0) / (x - x0)
    return m


# def equaçãoReta(x0, y0, x, y):


def acimaReta(x, y, xR, yR):
    if x >= xR and y >= yR:
        return True
    else:
        return False

def abaixoReta(x, y, xR, yR):
    if x <= xR and y <= yR:
        return True
    else:
        return False

def alturaL(y, y0):
    h = y - y0
    return h

def diâmetroMenor(y, y0):
    d = alturaL(y, y0) * 2
    return d

def diâmetroMaior(y, y0):
    D = diâmetroMenor(y, y0) * 2
    return D

def pertLosango(x, y, xe, ye, xs, ys):
    h = alturaL(ye, ys)
    d = diâmetroMenor(ye, ys)
    D = diâmetroMaior(ye, ys)

    yf = ye
    xf = xe + D

    xt = xs
    yt = ys - d

    if abaixoReta(x, y, xe, ye)
