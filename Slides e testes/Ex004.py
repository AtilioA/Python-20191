# 6) Dada a idade de uma pessoa em segundos e um planeta do sistema solar, calcule
# qual seria a idade relativa dessa pessoa no planeta informado, sabendo que o
# Período Orbital é o intervalo de tempo que o planeta leva para executar uma
# órbita em torno do Sol (o que é denominado de ano, que na Terra tem
# aproximadamente 365,25 dias). Considere então as informações abaixo para outros
# planetas do sistema solar:

def idadeDias(idadeAnos, planeta):
    try:
        if planeta.lower() in "terra":
            idadeD = idade * 365.25
            return idadeD

        elif planeta.lower() in "mercúrio":
            idadeD = idade * 0.2408467
            return idadeD

        elif planeta.lower() in "vênus":
            idadeD = idade * 0.61519726
            return idadeD

        elif planeta.lower() in "marte":
            idadeD = idade * 1.8808158
            return idadeD


        elif planeta.lower() in "júpiter":
            idadeD = idade * 11.862615
            return idadeD


        elif planeta.lower() in "saturno":
            idadeD = idade * 29.447498
            return idadeD


        elif planeta.lower() in "urano":
            idadeD = idade * 84.016846
            return idadeD


        elif planeta.lower() in "netuno":
            idadeD = idade * 164.79132
            return idadeD

        else:
            print("Entrada inválida.")
            raise exception()

    except: pass

def idadeRelativa(idade, planeta):

    try:
        if planeta.lower() in "terra":
            return idade
        elif planeta.lower() in "mercúrio":
            idadeR = idade / 0.2408467
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos mercurianos: {:.5f}.\nIdade em dias mercurianos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "vênus":
            idadeR = idade / 0.61519726
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos venusianos: {:.5f}.\nIdade em dias venusianos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "marte":
            idadeR = idade / 1.8808158
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos marcianos: {:.5f}.\nIdade em dias marcianos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "júpiter":
            idadeR = idade / 11.862615
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos jupiterianos: {:.5f}.\nIdade em dias jupiterianos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "saturno":
            idadeR = idade / 29.447498
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos saturninos: {:.5f}.\nIdade em dias saturninos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "urano":
            idadeR = idade / 84.016846
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos uraninanos: {:.5f}.\nIdade em dias uraninanos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        elif planeta.lower() in "netuno":
            idadeR = idade / 164.79132
            idadeD = idadeDias(idadeR, planeta)

            print("Idade em anos netunianos: {:.5f}.\nIdade em dias netunianos: {:.2f}.\n".format(idadeR, idadeD))

            return idadeR

        else:
            print("Entrada inválida.")
            raise exception()

    except: pass

# Terra: período orbital: 365.25 dias na Terra, ou 31557600 segundos
# Mercúrio: período orbital: 0.2408467 anos na Terra
# Vênus: período orbital: 0.61519726 anos na Terra
# Marte: período orbital: 1.8808158 anos na Terra
# Júpiter: período orbital: 11.862615 anos na Terra
# Saturno: período orbital: 29.447498 anos na Terra
# Urano: período orbital: 84.016846 anos na Terra
# Netuno: período orbital: 164.79132 anos na Terra

idadeRelativa(18.7, "terra")
idadeRelativa(18.7, "mercúrio")
idadeRelativa(18.7, "vênus")
idadeRelativa(18.7, "marte")
idadeRelativa(18.7, "júpiter")
idadeRelativa(18.7, "saturno")
idadeRelativa(18.7, "urano")
idadeRelativa(18.7, "netuno")
