import time
import os
from classes.class_personagens import Inimigo
from classes.class_batalha import Batalha

class Historia:
    def __init__(self, jogador):
        self.jogador = jogador

    def digitar(self, texto, velocidade=0.05):
        for letra in texto:
            print(letra, end='', flush=True)
            if letra == "\n":
                time.sleep(velocidade * 5)
            else:
                time.sleep(velocidade)

    # Fluxo de escolha porta antiga
    def _escolherPortaAntiga(self):
        os.system('cls')
        self.digitar("No fundo da sala, uma figura de estatura média se destaca na penumbra..." \
        "\nSua pele esverdeada reflete a pouca luz, e em uma das mãos ela segura uma lâmina curta e gasta..." \
        "\nÀ medida que você se aproxima, a criatura se move — é um goblin..." \
        "\nO goblin solta um rosnado baixo, assume uma postura agressiva e ergue a arma..." \
        "\nVocê se prepara para o combate.")
        time.sleep(2)

        # Batalha       
        Goblin = Inimigo(15, 10, 10, "GOBLIN")
        Batalhar = Batalha(self.jogador, Goblin)
        Batalhar.combate(self.jogador, Goblin, self.jogador.arma_escolhida.dano, Goblin.dano, self.jogador.defesa, Goblin.defesa)
        time.sleep(2)
        os.system('cls')

    # Fluxo de escolha caminho estreito
    def _escolherCaminhoEstreito(self):
        print("")
        
    def iniciarHistoria(self):
        os.system('cls')
        time.sleep(0.8)
        print("-------INÍCIO DA HISTÓRIA-------")
        time.sleep(0.8)
        self.digitar("\nVocê desperta com a cabeça latejando em uma caverna úmida e parcialmente iluminada..." \
        "\nO silêncio é quebrado apenas pelo eco distante de gotas caindo..." \
        "\nÀ sua esquerda, uma porta antiga e desgastada parece guardar segredos esquecidos..." \
        "\nÀ sua direita, uma passagem estreita se estende pela escuridão, convidando — ou ameaçando — quem ousar seguir adiante..." \
        "\n\n1 - Porta Antiga  2 - Passagem Estreita")
        time.sleep(1)
        escolherPassagem = input("\n\nQual será o seu próximo passo? ")    
        print()    
        self.digitar("...", 1)
        time.sleep(0.8)
        match escolherPassagem:
            case "1":
                self._escolherPortaAntiga()
            case "2": 
                self._escolherCaminhoEstreito()
                print("Você escolheu o caminho estreito")
            case _:
                while True:
                    comando = input("\nEscolha uma alternativa válida: ")
                    if comando == "1" or comando == "2":
                        break

        