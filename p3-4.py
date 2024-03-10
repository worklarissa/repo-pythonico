#Faça um programa que peça 2 números inteiros e um número float.Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo
#A soma do triplo do primeiro com o terceiro
#o terceiro elevado ao cubo

primeiro = int(input("Digite um número inteiro: "))
segundo = int(input("Digite um número inteiro: "))
terceiro = float(input("Digite um número float: "))
print(primeiro, segundo, terceiro)

exercicio_um = ((2 * primeiro) * (segundo / 2))
print(f'Resultado um: {exercicio_um}')

exercicio_dois = ((3 * primeiro) + terceiro)
print(f'Resultado dois: {exercicio_dois}')

exercicio_tres = terceiro ** 3
print(f'Resultado três:{exercicio_tres}')