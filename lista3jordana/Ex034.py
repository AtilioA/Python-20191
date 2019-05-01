# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
# abaixo) e 3% para o Sindicato. O FGTS corresponde a 11% do Salário Bruto, mas não é
# descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
# quantidade de horas trabalhadas no mês.

# a. Desconto do IR:
# i. Salário Bruto até 900 (inclusive) - isento
# ii. Salário Bruto até 1500 (inclusive) - desconto de 5%
# iii. Salário Bruto até 2500 (inclusive) - desconto de 10%
# iv. Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações.


def descontoIR(salário):
    if salário <= 900:
        return 0
    elif salário <= 1500:
        return salário * 0.05
    elif salário <= 2500:
        return salário * 0.1
    else:
        return salário * 0.2

def descontoSindicato(salário):
    desconto = salário * 0.03
    return desconto

def depósitoFGTS(salário):
    valorADepositar = salário * 0.11
    return valorADepositar

def salário(horas, valorHora):
    salário = horas * valorHora
    return salário

def folhaDePagamento():
    horas = int(input("Informe o número de horas trabalhadas no mês: "))
    valorHora = float(input("Informe o valor da hora: "))

    salárioBruto = salário(horas, valorHora)

    ir = descontoIR(salárioBruto)
    sindicato = descontoSindicato(salárioBruto)
    fgts = depósitoFGTS(salárioBruto)

    salárioLíquido = salárioBruto - ir - sindicato

    print("\nSalário bruto: {}".format(salárioBruto))
    print("Desconto IR: {}".format(ir))
    print("Desconto sindicato: {}".format(sindicato))
    print("Valor a depositar ao FGTS: {}".format(fgts))
    print("Salário líquido: {}".format(salárioLíquido))

    return salárioLíquido

folhaDePagamento()
