def preçoPassagem(totalPassagem, idadePassageiro):
    if idadePassageiro >= 60:
        preço = totalPassagem * 0.60
    elif 2 <= idadePassageiro < 10:
        preço = totalPassagem * 0.50
    elif idadePassageiro < 2:
        preço = totalPassagem * 0.10
    else:
        preço = totalPassagem

    return preço

# print(preçoPassagem(1000, 1))
# print(preçoPassagem(1000, 2))
# print(preçoPassagem(1000, 9))
# print(preçoPassagem(1000, 10))
# print(preçoPassagem(1000, 11))
# print(preçoPassagem(1000, 59))
# print(preçoPassagem(1000, 60))
# print(preçoPassagem(1000, 100))
