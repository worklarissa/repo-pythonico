print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 42
total_tentativas= 3
rodada = 1

while(rodada <= total_tentativas):
    print(f"Tentativa: {rodada} de {total_tentativas}")
    chute_ = input("Digite o seu número: ")
    print("Você digitou: ", chute_)
    chute = int(chute_)
    
    acertou = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (chute < numero_secreto):
            print("Você errou, o número é maior")
        elif (chute > numero_secreto):
            print("Você errou, o numero secreto é menor")
        
    rodada = rodada + 1

print("Fim de jogo")

