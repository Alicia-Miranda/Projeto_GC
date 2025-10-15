import random

def jogar():
    numero_secreto = random.randint(1, 10)
    tentativas = 3
    print("--- Jogo da Adivinhação ---")
    print("Tente adivinhar um número entre 1 e 10.")

    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}")
        
        try:
            chute = int(input("Seu chute: "))
        except ValueError:
            print("Digite apenas números.")
            continue
            
        if chute < 1 or chute > 10:
            print("O número deve ser entre 1 e 10!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print(f"Parabéns! Você acertou o número secreto ({numero_secreto})!")
            break
        elif rodada < tentativas:
            if maior:
                print("Seu chute foi alto. Tente um número menor.")
            else:
                print("Seu chute foi baixo. Tente um número maior.")
        else:
            print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogar()