import forca
import adivinhacao


def escolha_jogo():
    while 1:
        print("**********************************")
        print("****Bem vindo a sala de jogos!****")
        print("**********************************")

        print("01 - Jogo da Forca")
        print("02 - Jogo da Advinhação")
        print("03 - Sair do jogo")
        jogo = int(input("Selecione qual jogo queres jogar?"))

        if(jogo == 1):
            forca.jogar()
        elif(jogo == 2):
            adivinhacao.jogar()
        elif(jogo == 3):
            break
        else:
            print("opção inválida")

        print("Fim do jogo")
        print("**********************************")

if(__name__ == "__main__"):

   escolha_jogo()