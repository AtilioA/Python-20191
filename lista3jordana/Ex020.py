# 3) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total.

def usoDeTinta(areaPintada):
    def tintaNecessaria(areaPintada):
        return areaPintada / 3

    def dinheiroNecessario(areaPintada):
        litrosTinta = tintaNecessaria(areaPintada)

        if (litrosTinta % 18 == 0):
            return (litrosTinta / 18) * 80
        else:
            return (litrosTinta // 18) + 1 * 80

    latas = tintaNecessaria(areaPintada)
    custo = dinheiroNecessario(areaPintada)

    print(f'Latas a serem compradas: {latas}')
    print(f'Preço total: R${custo}')
