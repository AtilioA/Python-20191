# 8) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a) Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# b) Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível, calcule e
# imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$
# 2,50 o preço do litro do álcool é R$ 1,90.

# 1 = álcool, 2 = gasolina


def valorPago(l, c):

    def valorÁlcool(l):
        try:
            if l <= 20:
                valor = l * 1.90 * 0.97
                return valor
            elif l > 20:
                valor = l * 1.90 * 0.95
                return valor
            else:
                raise exception()
        except: pass

    def valorGasolina(l):
        try:
            if l <= 20:
                valor = l * 2.50 * 0.96
                return valor
            elif l > 20:
                valor = l * 2.50 * 0.94
                return valor
            else:
                raise exception()
        except: pass

    if c == 1:
        valor = valorÁlcool(l)
        print("Valor a ser pago: R${:.2f}".format(valor))
        return valorÁlcool(l)
    elif c == 2:
        valor = valorGasolina(l)
        print("Valor a ser pago: R${:.2f}".format(valor))
        return valorGasolina(l)

valorPago(21, 1)
valorPago(21, 2)
