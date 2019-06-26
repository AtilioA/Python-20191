# O Zodíaco chinês é composto por animais com ciclo de 12 anos.
# Uma maneira simplificada # de identificá-lo é
# verificando-se apenas o ano de seu nascimento do seguinte modo:
# [...]

def lista_signos():
    signos = ['macaco', 'galo', 'cão', 'porco', 'rato', 'boi', 'tigre', 'coelho', 'dragão', 'serpente', 'cavalo', 'carneiro']
    return signos


def lista_aniversario():
    nDatas = int(input("Quantas datas de aniversário deseja informar? "))

    def informa_datas(aniversarios, nDatas):
        if nDatas < 1:
            return []
        else:
            data = int(input("Informe o ano de nascimento: "))
            return [data] + informa_datas(aniversarios, nDatas - 1)

    return informa_datas([0], nDatas)


def calcula_signos(lista, signos):
    if not lista:
        return []
    else:
        indiceSigno = lista[0] % 12
        return [signos[indiceSigno]] + calcula_signos(lista[1:], signos)


# aniversarios = [1999, 2000, 2001, 2019, 2020, 2049, 2077]
aniversarios = lista_aniversario()
print(aniversarios)
signos = lista_signos()
print(calcula_signos(aniversarios, signos))
