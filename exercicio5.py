# Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área
# do terreno. A leitura dos valores deve ser em metros e o cálculo realizado em
# metros.


largura = float(input('digite a largura em metros do terreno: '))
comprimento = float(input('digite o comprimento em metros do terreno: '))

def area(largura,comprimento):
    area = largura * comprimento
    return area

a = area(largura,comprimento)

print(f'a área do terreno é:',a,'m')


