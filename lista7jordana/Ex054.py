# Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas
# pelas demais pessoas

# Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
# Faça a função "traduzir", que recebe uma lista com uma mensagem (lSecreta) e "traduz" a
# sequência armazenada em lSecreta de acordo com o código das amigas.
# Teste para lSecreta = [2,15,13,0,4,9,1];
# Saída: ‘bom dia’


def decifra(criptografado, chave):
    try:
        if criptografado > 26 or criptografado < 0:
            print("Código inválido")
        else:
            alfabeto = " abcdefghijklmnopqrstuvwxyz"

            return alfabeto[criptografado + chave]
    except ValueError:
        pass


def traduzir(lSecreta):
    lista = list(map(lambda x: decifra(x, 0), lSecreta))
    string = ''.join(lista)
    return string


lSecreta = [2, 15, 13, 0, 4, 9, 1]
print(traduzir(lSecreta))
