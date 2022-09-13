import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")


numero_secreto = random.randrange(1, 11)

total_de_tentativas = 3
chute = 99999

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 10: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 10):
        print("Você deve digitar um número entre 1 e 10.")
        continue

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    elif(chute_maior):
        print("Você errou! O seu chute foi maior do que o numero secreto.")
    elif(chute_menor):
        print("Você errou! O seu chute foi menor do que o numero secreto.")
    else:
        print("error")


print("O numero secreto era", numero_secreto)
print("Fim do jogo")
