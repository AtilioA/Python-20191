# 6) Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo. O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem “APROVADO” se o conceito for A,B ou C e “REPROVADO”
# se o conceito for D ou E.E


def conceitoAluno(média):
    try:

        if 9 < média <= 10:
            return 'A'
        elif 7.5 < média <= 9:
            return 'B'
        elif 6 < média <= 7.5:
            return 'C'
        elif 4 < média <= 6:
            return 'D'
        elif 0 < média <= 4:
            return 'E'
        else:
            raise exception()

    except:
        pass


def médiaAluno(n1, n2):
    média = (n1 + n2) / 2
    return média


def foiAprovado(conceito):
    if str(conceito) < 'C':
        return True
    else:
        return False


def SituaçãoAluno(n1, n2):
    média = médiaAluno(n1, n2)
    foiAprovado(média)
    conceito = conceitoAluno(média)

    print("Média de aproveitamento: {}".format(média))
    print("Conceito: {}".format(conceito))

    print("Foi aprovado?")
    if foiAprovado(conceito):
        print("SIM")
    else:
        print("NAO")
