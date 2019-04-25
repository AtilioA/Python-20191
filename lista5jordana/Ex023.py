# Em uma loja de bugingangas, os produtos são divididos em classes que determinam o
# seu preço. As vendas são feitas apenas no atacado, havendo quantidade mínima e
# máxima determinadas. Além disso, há descontos progressivos para compras maiores. A
# determinação do preço unitário é discriminada a seguir. Determine, dados a classe e a
# quantidade de produtos, qual o preço a ser pago.

def éAtacado(qtdMínima, qtdMáxima, qtd):
    if qtd < qtdMínima:
        print("Não é possível realizar a compra. Quantidade mínima não foi alcançada.")
        return False
    elif qtd > qtdMáxima:
        print("Não é possível realizar a compra. Quantidade máxima ultrapassada.")
        return False
    else:
        return True

def classe1(qtd):
    qtdMínima = 20
    qtdMáxima = 80

    try:
        if not éAtacado(qtdMínima, qtdMáxima, qtd):
            raise exception()
        else:
            if qtd < 40:
                preçoTotal = qtd * 2.0
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 40 and qtd < 60:
                preçoTotal = qtd * 1.90
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 60 and qtd < 80:
                preçoTotal = qtd * 1.80
                print("Preço total a pagar: {}.". format(preçoTotal))
    except: pass

def classe2(qtd):
    qtdMínima = 10
    qtdMáxima = 60

    try:
        if not éAtacado(qtdMínima, qtdMáxima, qtd):
            raise exception()
        else:
            if qtd < 20:
                preçoTotal = qtd * 5.0
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 20 and qtd < 40:
                preçoTotal = qtd * 4.75
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 40 and qtd < 60:
                preçoTotal = qtd * 4.50
                print("Preço total a pagar: {}.". format(preçoTotal))
    except: pass

def classe3(qtd):
    qtdMínima = 5
    qtdMáxima = 50

    try:
        if not éAtacado(qtdMínima, qtdMáxima, qtd):
            raise exception()
        else:
            if qtd < 10:
                preçoTotal = qtd * 8.0
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 20 and qtd < 40:
                preçoTotal = qtd * 7.60
                print("Preço total a pagar: {}.". format(preçoTotal))
            elif qtd >= 40 and qtd < 60:
                preçoTotal = qtd * 7.20
                print("Preço total a pagar: {}.". format(preçoTotal))
    except: pass


# Testes:
classe1(10)
classe1(20)
classe1(30)
classe1(40)
classe1(60)
classe1(80)
classe1(81)

classe2(10)
classe2(20)
classe2(30)
classe2(40)
classe2(60)
classe2(80)
classe2(81)

classe3(10)
classe3(20)
classe3(30)
classe3(40)
classe3(60)
classe3(80)
classe3(81)
#
