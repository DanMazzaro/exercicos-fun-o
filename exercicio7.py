# Escreva uma funcão em Python que recebe uma lista e retorna uma outra
# lista contendo apenas os elementos que aparecem duas ou mais vezes na lista
# de entrada.

def eleme_rep(lista):
    repetidos = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                if lista[i] not in repetidos:
                    repetidos.append(lista[i])
                break
    return repetidos

entrada = input('digite os elementos da lista separados por um espaço: ')


lista = [int(x) for x in entrada.split()]


saida = eleme_rep(lista)
print('elementos que se repetem:', saida)