# 1) Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendose que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
# sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido.


def descontaSindicato(salario):
    salarioDescontado = salario * 0.05
    return salarioDescontado


def descontaINSS(salario):
    salarioDescontado = salario * 0.08
    return salarioDescontado


def descontaIR(salario):
    salarioDescontado = salario * 0.11
    return salarioDescontado


def descontaTudo(salario):
    descontoIR = descontaIR(salario)
    descontoINSS = descontaINSS(salario)
    descontoSindicato = descontaSindicato(salario)
    descontoTotal = descontoIR + descontoINSS + descontoSindicato

    return descontoTotal


def descontaSalario(salarioBruto):
    salarioLiquido = salarioBruto

    desconto = descontaTudo(salarioBruto)

    salarioLiquido = salarioLiquido - desconto

    return salarioLiquido


def salario(ganhoHora, nHoras):

    def descontado(salarioBruto, salarioLiquido):
        return salarioBruto - salarioLiquido

    salarioBruto = ganhoHora * nHoras
    salarioLiquido = descontaSalario(salarioBruto)

    descontoIR = descontaIR(salarioBruto)
    descontoINSS = descontaINSS(salarioBruto)
    descontoSindicato = descontaSindicato(salarioBruto)
    descontoTotal = descontaTudo(salarioBruto)

    print(f"Desconto INSS: {descontoINSS}")
    print(f"Desconto sindicato: {descontoSindicato}")
    print(f"Desconto total: {descontoTotal}")
    print(f"Salário bruto: {salarioBruto}")
    print(f"Salário líquido: {salarioLiquido}")

    return salarioLiquido
