# Faça um código que recebe os valores inteiros digitados pelo usuário e
# armazena esses valores em um vetor. Para armazenar e mostrar os valores
# armazenados utilize uma função.

valores = []
vetor = [ ]

def resultado (vetor):
    vetor = valores
    del vetor[-1]
    return vetor


while True:
    valor = input('digite um valor: ')
    valores.append(valor)
    if valor == 'pronto':
        break

resposta = resultado(vetor)

print(resposta)