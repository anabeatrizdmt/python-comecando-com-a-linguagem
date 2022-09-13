import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")
print("Adivinhe o número secreto entre 1 e 10")
print("*********************************")

numero_secreto = random.randrange(1, 11)

total_de_tentativa = 3
rodada = 1
chute=99999

while(rodada<=total_de_tentativa):  # | chute != numero_secreto
    if(chute != numero_secreto):
        print("Tentativa",rodada,"de", total_de_tentativa)
        chute_str = input("Digite o seu número: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Você acertou!")
        elif(chute_maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o numero secreto.")
        else:
            print("error")

        rodada += 1
    else:
        break

print("O numero secreto era", numero_secreto)
print("Fim do jogo")
