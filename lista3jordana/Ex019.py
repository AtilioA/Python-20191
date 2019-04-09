# 2) Tendo como dado de entrada a altura (h) de uma pessoa e seu gênero (g), construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

def pesoIdeal(altura, genero):
    def pesoIdealHomem(altura):
        return (72.7 * altura) - 58
    def pesoIdealMulher(altura):
        return (62.1 * altura) - 44.7

    if genero in "Hh":
        return pesoIdealHomem(altura)

    if genero in "Mm":
        return pesoIdealMulher(altura)
