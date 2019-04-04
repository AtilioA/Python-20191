def cedulaAcima(y):
    if (y + 1 >= 8):
        return False
    else:
        return True

def cedulaAbaixo(y):
    if (y - 1 <= 0):
        return False
    else:
        return True

def cedulaEsquerda(x):
    if (x - 1 <= 0):
        return False
    else:
        return True

def cedulaDireita(x):
    if (x + 1 >= 8):
        return False
    else:
        return True

def cedulaDSupEsq(x, y):
    if (x - 1 <= 0) or (y + 1 >= 8):
        return False
    else:
        return True

def cedulaDSupDir(x, y):
    if (x + 1 >= 8) or (y + 1 >= 8):
        return False
    else:
        return True

def cedulaDInfEsq(x, y):
    if (x - 1 <= 0) or (y - 1 <= 0):
        return False
    else:
        return True

def cedulaDInfDir(x, y):
    if (x + 1 >= 8) or (y - 1 <= 0):
        return False
    else:
        return True


def posValida(x, y):
    if x < 1 or y < 1:
        return False
    elif x > 8 or y > 8:
        return False
    else:
        return True

def tabuleiro(x, y):
    if (posValida(x, y)):
        print("A posicao e valida!")
        if cedulaAcima(y):
            print("A peca pode se mover para cima")
        if cedulaAbaixo(y):
            print("A peca pode se mover para baixo")
        if cedulaEsquerda(x):
            print("A peca pode se mover para a esquerda")
        if cedulaDireita(x):
            print("A peca pode se mover para a direita")
        if cedulaDSupEsq(x, y):
            print("A peca pode se mover para a diagonal superior esquerda")
        if cedulaDSupDir(x, y):
            print("A peca pode se mover para a diagonal superior direita")
        if cedulaDInfEsq(x, y):
            print("A peca pode se mover para a diagonal inferior esquerda")
        if cedulaDInfDir(x, y):
            print("A peca pode se mover para a diagonal inferior direita")
        return True
    else:
        return False

# tabuleiro(8, 8)
