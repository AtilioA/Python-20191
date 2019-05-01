# 3.1. A expressão que calcula o volume da figura. Faça o modelo de avaliação da expressão.
import math as jordana

def vCilindro(r, h):
    v = jordana.pi * r ** 2 * h
    return v;

def vSemiCilindro(r, h):
    v = vCilindro(r, h) / 2
    return v;

def volumeFigura(rMenor, rMaior, alturaEmPe, larguraEmPe, alturaDeitada, comprimentoDeitada, larguraCirculos, saliencia, salienciaSemiCilindro):
    larguraAmbas = rMenor * 2 + saliencia * 2

    volumeTotalDeitada = (comprimentoDeitada - larguraCirculos) * alturaDeitada * larguraAmbas
    volumeSemiCilindroDeitado = vSemiCilindro(rMenor, alturaDeitada) + salienciaSemiCilindro * alturaDeitada * rMenor * 2
    volumeDeitadaReal = volumeTotalDeitada - volumeSemiCilindroDeitado

    volumeSemiCilindroMaior = vSemiCilindro(rMaior, rMenor) - vSemiCilindro(rMenor, rMenor)
    volumeExtra = salienciaSemiCilindro * alturaDeitada * rMenor * 2
    volumeTotalEmPé = volumeDeitadaReal + volumeExtra + volumeSemiCilindroMaior

    volumeTotal = volumeTotalEmPé + volumeDeitadaReal

    return volumeTotal


# 3.2. Uma abstração para a expressão encontrada no item 1.

# 3.3. Uma versão generalizada da abstração do item anterior.
# Faça o modelo de avaliação para a instanciação proposta no exercício.
/
