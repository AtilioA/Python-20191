# 8) O bispo, no jogo do xadrez, é uma peça que movimenta -se nas diagonais sobre as quais ela está posicionada.

# Dado um tabuleiro de dimensões 8x8 e uma posição do bispo no tabuleiro, faça uma função que:
# 1 - verifique se o movimento válido é para a direita ou para a esquerda. Lembre-se que o movimento deve ser aplicado apenas se a posição inicial é válida, ou seja, deve estar dentro do tabuleiro.

# O tipo da resposta da sua função é Char. Ela deve responder 'D' se o movimento a ser feito é para a direita; 'E', se o movimento deve ser para a esquerda e '0', se a posição original não é válida.

from Ex011 import posValida

def bispoEsquerdaDireita(x, y):
    if (posValida(x, y) == False):
        print("A posição original não é válida")
        return '0'


# print(bispoEsquerdaDireita(-2, 1))
# print(bispoEsquerdaDireita(1, 1))
