print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 42

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
    elif (chute > numer_secreto):
        print("Você errou, o numero secreto é menor")
print("Fim de jogo")

