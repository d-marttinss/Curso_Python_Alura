import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***********************************")

    print("Nivel 1 - Fácil")
    print("Nivel 2 - Médio")
    print("Nivel 3 - Dificil")
    nivel = int(input("Em qual nivel você quer jogar?"))

    numero_correto = random.randrange(1, 101)
    pontos = 1000

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range (1, total_de_tentativas + 1) :
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite o número que você acha que é entre 0 e 100:"))

        if(chute < 1 or chute > 100):
            print("Você digitou um número fora do solicitado")
            continue

        acerto = chute == numero_correto
        numero_maior = chute > numero_correto
        numero_menor = chute < numero_correto

        if(acerto):
            print(f"você acertou! Pontuação {pontos}")
            break
        else:
            if(numero_maior):
                print("Você errou! Seu numero foi maior que o número correto")
            elif(numero_menor):
                print("Você errou! Seu numero foi menor que o número correto")
        pontuacao_perdida = abs(numero_correto - chute)
        pontos -= pontuacao_perdida
        rodada += 1

    print("Fim do jogo")
    print("*********************************")

if(__name__ == "__main__"):
    jogar()