# Faça um código que recebe valores inteiros digitados pelo usuário e
# armazena os valores pares em um vetor e os ímpares em outro vetor. Utilize
# função para verificar se é par ou ímpar e para armazenar e mostrar os valores.

pares = []
impares = []

def verifica_par_impar(numero):
    """Função que verifica se um número é par ou ímpar"""
    return numero % 2 == 0 in pares
    
    while True:
        entrada = input("Digite um número inteiro (ou 's' para sair): ")
        
        if entrada.lower() == 's':
            break
            
        try:
            numero = int(entrada)
            if verifica_par_impar(numero):
                pares.append(numero)
                print(f"Número {numero} é par e foi adicionado ao vetor de pares.")
            else:
                impares.append(numero)
                print(f"Número {numero} é ímpar e foi adicionado ao vetor de ímpares.")
        except ValueError:
            print("Por favor, digite um número inteiro válido ou 's' para sair.")
    
    return pares, impares

def mostrar_valores(pares, impares):
    """Função para mostrar os valores armazenados"""
    print("\nValores armazenados:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Programa principal
def main():
    print("Separador de números pares e ímpares")
    print("-------------------------------------")
    
    pares, impares = armazenar_numeros()
    mostrar_valores(pares, impares)

if __name__ == "__main__":
    main()