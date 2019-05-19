# 11) Dada uma string (lista de caracteres), verificar se é um palíndromo (a string é a mesma
# quando lida da esquerda para a direita ou da direita para a esquerda, ex:
# “arara” – observe que a string vazia é dada por "" ao invés de [ ] ).

def reverteString(string):
    revertida = string[::-1]
    return revertida

def éPalíndromo(string):
    revertida = reverteString(string)
    if string == revertida:
        return True
    else:
        return False
