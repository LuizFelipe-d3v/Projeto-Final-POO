import time
import os

class Historia:
    def iniciarHistoria(self):
        os.system('cls')
        time.sleep(0.7)
        print("-------INÍCIO DA HISTÓRIA-------")
        print("")
        print("Você desperta com a cabeça latejando em uma caverna úmida e parcialmente iluminada...")
        time.sleep(3.5)
        print("O silêncio é quebrado apenas pelo eco distante de gotas caindo...")
        time.sleep(3.5)
        print("À sua esquerda, uma porta antiga e desgastada parece guardar segredos esquecidos...")
        time.sleep(1)
        print("À sua direita, uma passagem estreita se estende pela escuridão, convidando — ou ameaçando — quem ousar seguir adiante...")
        time.sleep(1)
        print("")
        print("1 - Porta Antiga  2 - Passagem Estreita")
        time.sleep(0.8)
        print("")
        escolherPassagem = input("Qual será o seu próximo passo? ")

        match escolherPassagem:
            case "1":
                print("Você escolheu a porta antiga")
            case "2": 
                print("Você escolheu o caminho estreito")