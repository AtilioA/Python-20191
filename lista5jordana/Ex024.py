# 3.1. A expressão que calcula o volume da figura. Faça o modelo de avaliação da expressão.
import math as jordana

def vCilindro(r, h):
    v = jordana.pi * r ** 2 * h
    return v

def vSemiCilindro(r, h):
    v = vCilindro(r, h) / 2
    return v

def volumeFigura(rMenor, rMaior, alturaEmPe, alturaDeitada, larguraCilindros, larguraTotal, saliência, saliênciaSemiCilindro):
    comprimentoAmbas = rMenor * 2 + saliência * 2

    volumeTotalDeitada = (larguraTotal - larguraCilindros) * alturaDeitada * comprimentoAmbas
    volumeSemiCilindroDeitado = vSemiCilindro(rMenor, alturaDeitada) + saliênciaSemiCilindro * alturaDeitada * rMenor * 2
    volumeDeitadaReal = volumeTotalDeitada - volumeSemiCilindroDeitado

    print(volumeDeitadaReal)

    volumeSemiCilindroMaior = vSemiCilindro(rMaior, larguraCilindros)
    volumeCirculoEmPé = vCilindro(rMenor, larguraCilindros)
    volumeArco = volumeSemiCilindroMaior - volumeCirculoEmPé
    volumeParalelepipedoEmPé = (alturaEmPe - rMaior) * larguraCilindros * comprimentoAmbas
    volumeEmPé = volumeArco + volumeParalelepipedoEmPé

    volumeTotal = volumeEmPé + volumeDeitadaReal

    return volumeTotal


# 3.2. Uma abstração para a expressão encontrada no item 1.

# 3.3. Uma versão generalizada da abstração do item anterior.
# Faça o modelo de avaliação para a instanciação proposta no exercício.

volumeFigura(10, 15, 40, 10, 10, 30, 5, 5)
# a(rMenor, rMaior, alturaEmPe, alturaDeitada, larguraCilindros, larguraTotal, saliência, saliênciaSemiCilindro):
