import random

def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 11) #ou podemos usar round(random.random() * 10)
    total_de_tentativas = 0
    pontos = 100

    print("Qual nível de dificuldade?")
    nivel = int(input("(1) Fácil (2) Médio (3) Difícil:"))

    if (nivel == 1):
        total_de_tentativas = 5
    elif (nivel == 2):
        total_de_tentativas = 3
    elif (nivel == 3):
        total_de_tentativas = 1

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
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o numero secreto.")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o numero secreto.")
            else:
                print("error")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("O numero secreto era", numero_secreto)
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()