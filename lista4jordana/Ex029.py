# O estúdio fotográfico Boa Imagem cobra de seus clientes por retratos antigos baseando se no número de indivíduos incluídos no retrato. As tarifas constam da tabela seguinte. Retratos antigos tirados aos sábados ou aos domings custam 20% a mais do que o preço base. Defina uma função que recebe como argumentos o número de pessoas no retrato
# e o dia da semana agendado, e calcula o custo do retrato.

def custoRetrato(nPessoas, diaSemana):
    try:
        if nPessoas == 1:
            custoPadrao = 100
        elif nPessoas == 2:
            custoPadrao = 130
        elif nPessoas == 3:
            custoPadrao = 150
        elif nPessoas == 4:
            custoPadrao = 165
        elif nPessoas == 5:
            custoPadrao = 175
        elif nPessoas == 6:
            custoPadrao = 180
        elif nPessoas >= 7:
            custoPadrao = 185
        else:
            print("Erro. Número de pessoas inválido")
            raise exception()
    except: pass

    try:
        if diaSemana == 6 or diaSemana == 7:
            custoFDS = custoPadrao * 1.20
            return custoFDS
        elif diaSemana >= 1 and diaSemana <= 5:
            return custoPadrao
        else:
            print("Erro. Dia da semana inválido")
            raise exception()
    except: pass
