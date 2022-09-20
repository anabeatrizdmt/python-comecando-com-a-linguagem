import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_espaco_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta)-erros))

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem-vindo ao jogo de forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo_palavras = open('palavras.txt', encoding='utf-8', mode='r')
    lista_palavras = []

    for linha in arquivo_palavras:
        linha = linha.strip()
        lista_palavras.append(linha)

    arquivo_palavras.close()

    numero = random.randrange(0,len(lista_palavras))
    palavra_secreta = lista_palavras[numero].strip().upper()
    return palavra_secreta

def inicializa_espaco_letras(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns! Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu. Tente novamente.")


if (__name__ == "__main__"):
    jogar()
