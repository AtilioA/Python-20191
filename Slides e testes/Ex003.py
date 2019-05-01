# 4) Uma empresa decidiu dar a seus funcionários um abono de natal. A
# gratificação será baseada em dois critérios: o número de horas extras
# trabalhadas e o número de horas que o empregado faltou ao trabalho.
#
# O critério estabelecido para calcular o prêmio é: subtrair dois terços das horas
# que o empregado faltou de suas horas extras, obtendo um valor que
# determina o número de pontos do funcionário. Faça uma função para calcular
# o abono de natal para cada funcionário. A distribuição do prêmio é feita de
# acordo com a tabela abaixo:

def pontosFuncionário(horasExtras, horasFaltas):
    pontos = horasExtras - horasFaltas
    return pontos

def bonificaçãoNatal(horasExtras, horasFaltas):
    pontos = pontosFuncionário(horasExtras, horasFaltas)

    if 1 <= pontos < 10:
        prêmio = 100
    elif 10 <= pontos < 20:
        prêmio = 200
    elif 20 <= pontos < 30:
        prêmio = 300
    elif 30 <= pontos < 40:
        prêmio = 400
    elif pontos >= 41:
        prêmio = 500
    else:
        prêmio = 0

    return prêmio
