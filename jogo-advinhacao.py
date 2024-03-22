print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 42
total_tentativas= 3


for rodada in range (1, total_tentativas + 1):
    print(f"Tentativa: {rodada} de {total_tentativas}")
    chute_ = input("Digite um número de 1 a 100: ")
    print("Você digitou: ", chute_)
    chute = int(chute_)
    
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número maior que 1 e menor quem 100")
        continue

    acertou = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (chute < numero_secreto):
            print("Você errou, o número é maior")
        elif (chute > numero_secreto):
            print("Você errou, o numero secreto é menor")
        

print("Fim de jogo")

