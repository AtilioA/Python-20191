# 4) As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calculará os
# reajustes. Faça um programa que recebe o salário de um colaborador faça o reajuste
# segundo o seguinte critério, baseado no salário atual:
# a. salários até R$ 280,00 (incluindo) : aumento de 20%
# b. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# c. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# d. salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# i. o salário antes do reajuste;
# ii. o percentual de aumento aplicado;
# iii. o valor do aumento;
# iv. o novo salário, após o aumento


def salárioAte280(salárioColaborador):
    salárioNovo = salárioColaborador * 1.20
    return salárioNovo


def salárioEntre280e700(salárioColaborador):
    salárioNovo = salárioColaborador * 1.15
    return salárioNovo


def salárioEntre700e1500(salárioColaborador):
    salárioNovo = salárioColaborador * 1.10
    return salárioNovo


def salárioMaiorQue1500(salárioColaborador):
    salárioNovo = salárioColaborador * 1.05
    return salárioNovo


def reajusteSalário(salárioColaborador):

    if (salárioColaborador <= 280):
        salárioNovo = salárioColaborador = salárioAte280(salárioColaborador)

    elif (salárioColaborador > 280 and salárioColaborador <= 700):
        salárioNovo = salárioEntre280e700(salárioColaborador)

    elif (salárioColaborador > 700 and salárioColaborador <= 1500):
        salárioNovo = salárioEntre700e1500(salárioColaborador)

    elif (salárioColaborador >= 1500):
        salárioNovo = salárioMaiorQue1500(salárioColaborador)

    # # i. o salário antes do reajuste;
    # ii. o percentual de aumento aplicado;
    # iii. o valor do aumento;
    # iv. o novo salário, após o aumento

    print("Salário antes do reajuste: {salárioAntigo}")
    print("Percentual do reajuste: {percentualReajuste}")
    print("Valor do reajuste: {valorReajuste}")
    print(f"Salário depois do reajuste: {salárioNovo}")

    return salárioNovo

# reajusteSalário(250)
