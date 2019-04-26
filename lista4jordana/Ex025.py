# Sabe-se que o quilowatt de energia elétrica custa um quinto do salário mínimo. Defina
# uma função que receba o valor do salário mínimo e a quantidade de quilowatts
# consumida por uma residência, e resulta no valor a ser pago com desconto de 15%.

def valorEnergia(salMin, kW):
    preçokW = salMin * (1 / 5)
    preçoTotal = preçokW * kW
    preçoDesconto = preçoTotal * 0.85
    return preçoDesconto
