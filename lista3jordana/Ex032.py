# 7) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2
# + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
# e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
# usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


def delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta


def raizSegundoGrau():
    try:

        a = int(input("Informe o valor de a: "))
        if a == 0:
            print("A equação não é de segundo grau.")
            raise exception()

        b = int(input("Informe o valor de b: "))
        c = int(input("Informe o valor de c: "))

        d = delta(a, b, c)

        if d < 0:
            print("A equação não possui raizes reais.")
            raise exception()
        elif d == 0:
            raiz = (- b + d) / 2 * a
            print("A equação possui apenas uma raiz real: {}".format(raiz))
            return raiz
        else:
            raiz1 = (- b + d) / 2 * a
            raiz2 = (- b - d) / 2 * a
            print("A equação possui duas raizes reais: {} e {}".format(raiz1, raiz2))
            return (raiz1, raiz2)

    except:
        pass
