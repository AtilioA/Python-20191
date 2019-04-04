import math

# A expressão que calcula o volume da figura. Faça o modelo de avaliação da expressão.
# Uma abstração para a expressão encontrada no item 1.

def areaSemiCirculo(raio):
    area = math.pi * raio ** 2 / 2

    return area

def areaParalelepipedo(largura, altura, comprimento):
    area = largura * altura * comprimento

    return area

# Uma versão generalizada da abstração do item anterior. Faça o modelo de avaliação para a instanciação proposta no exercício:
def volumeFigura(altura, largura, raio, ladoParalele, saliencia):
    diametro = raio * 2
    comprimentoTotal = diametro + saliencia * 2
    areaTotal = areaParalelepipedo(largura, altura, comprimentoTotal)

    areaSemiCirc = areaSemiCirculo(raio) * altura
    areaParalelepipedin = areaParalelepipedo(ladoParalele, altura, diametro)

    area = areaTotal - areaSemiCirc - areaParalelepipedin

    return area

print("Instanciação de volumeFigura: {:g}".format(volumeFigura(10, 20, 10, 5, 5)))
