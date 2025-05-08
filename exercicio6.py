# Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem, e custo, que é o custo de um item
# antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas. Mostre o valor final.

taxaImposto = float(input('qual a taxa de imposto? '))
custo = float(input('qual o custo do produto? ' ))


def somaImposto(taxaImposto, custo):
    calculo = (taxaImposto/100) * custo
    return custo + calculo

print(f'o valor final do produto com o imposto adicionado é:',somaImposto(taxaImposto, custo))