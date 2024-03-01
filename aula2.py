print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 42

chute_ = input("Digite o seu número: ")
print("Você digitou: ", chute_)
chute = int(chute_)

if (chute == numero_secreto):
    print("Você acertou")
else:
    print("Você errou")

print("Fim de jogo")

