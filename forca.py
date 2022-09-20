import random
def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo de forca!***")
    print("*********************************")

    arquivo_palavras = open('palavras.txt', encoding='utf-8', mode='r')
    lista_palavras = []

    for linha in arquivo_palavras:
        linha = linha.strip()
        lista_palavras.append(linha)

    arquivo_palavras.close()

    numero = random.randrange(0,len(lista_palavras))
    palavra_secreta = lista_palavras[numero].strip().upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    # letras_acertadas = []
    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta)-erros))

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns! Você ganhou!")
    else:
        print("Você perdeu. Tente novamente.")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()