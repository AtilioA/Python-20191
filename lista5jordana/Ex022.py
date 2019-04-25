import math

def distEuclid(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def contidoCirculo(xp, yp, xc, yc, r):
    if (distEuclid(xp, yp, xc, yc) <= r * math.sqrt(2)): # ???
        return True
    else:
        return False

def pertinenciaCirculos(xp, yp, xc, yc, rMaior):
    rMenor = rMaior / 2

    def contidoCirculoAbaixo(xp, yp, xc, yc, rMenor):
        if (contidoCirculo(xp, yp, xc, yc - rMenor, rMenor)):
            return True
        else:
            return False

    def contidoCirculoAcima(xp, yp, xc, yc, rMenor):
        if (contidoCirculo(xp, yp, xc, yc + rMenor, rMenor)):
            return True
        else:
            return False

    def contidoCirculoDireita(xp, yp, xc, yc, rMenor):
        if (contidoCirculo(xp, yp, xc + rMaior, yc, rMenor)):
            return True
        else:
            return False

    def contidoCirculoEsquerda(xp, yp, xc, yc, rMenor):
        if (contidoCirculo(xp, yp, xc - rMenor, yc, rMenor)):
            return True
        else:
            return False

    def contidoAcimaCirculoDireita(xp, yp, xc, yc, rMaior, rMenor):
        if (xp >= xc) and (yp >= yc) and contidoCirculo(xp, yp, xc, yc, rMaior):
            if contidoCirculoDireita(xp, yp, xc, yc, rMenor):
                if contidoCirculoAcima(xp, yp, xc, yc, rMenor):
                    return True
                else:
                    return False

    def contidoAbaixoCirculoEsquerda(xp, yp, xc, yc, rMaior, rMenor):
        if (xp <= xc) and (yp <= yc) and contidoCirculo(xp, yp, xc, yc, rMaior):
            if contidoCirculoEsquerda(xp, yp, xc, yc, rMenor):
                if contidoCirculoAbaixo(xp, yp, xc, yc, rMenor):
                    return True
                else:
                    return False

    if not contidoCirculo(xp, yp, xc, yc, rMaior):
        print("Não está contido. Não está no círculo maior.")
        return False
    elif contidoCirculoAbaixo(xp, yp, xc, yc, rMenor) or contidoCirculoAbaixo(xp, yp, xc, yc, rMenor) or contidoAbaixoCirculoEsquerda(xp, yp, xc, yc, rMaior, rMenor) or contidoAcimaCirculoDireita(xp, yp, xc, yc, rMaior, rMenor):
        print("Não está contido.")
        return False
    else:
        print("Está contido.")
        return True

pertinenciaCirculos(100, 100.1, 0, 0, 100)
