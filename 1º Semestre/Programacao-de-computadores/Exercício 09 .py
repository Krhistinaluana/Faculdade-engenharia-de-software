#Estrutura de repetições
#Jogo de adivinhar senha
#

def iniciar_jogo():
    import random       

    numero_secreto = random.randint(1, 10)

    return numero_secreto

def verificar_numero(numero_secreto, numero_jogador):
    if numero_jogador == numero_secreto:
        return True
    else:
        return False    
    
numero_secreto = iniciar_jogo()

acertou = False

while acertou == False:
    numero_jogador = int(input("Digite um número entre 1 e 10: "))
    acertou = verificar_numero(numero_secreto, numero_jogador)

    if acertou:
        print()
        print("Parabéns, você acertou o número secreto!")
    else:
        print()
        print("Número incorreto, tente novamente!")
