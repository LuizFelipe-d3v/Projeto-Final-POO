import time
import os

class Historia:
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
        self.digitar("No fundo da sala, uma figura de estatura média se destaca na penumbra...")
        time.sleep(2)
        self.digitar("\nSua pele esverdeada reflete a pouca luz, e em uma das mãos ela segura uma lâmina curta e gasta...")
        time.sleep(2)
        self.digitar("\nÀ medida que você se aproxima, a criatura se move — é um goblin...")
        time.sleep(2)
        self.digitar("\nO goblin solta um rosnado baixo, assume uma postura agressiva e ergue a arma...")
        time.sleep(1.5)
        self.digitar("\nVocê se prepara para o combate.")

    # Fluxo de escolha caminho estreito
    def _escolherCaminhoEstreito(self):
        print("")
        
    def iniciarHistoria(self):
        os.system('cls')
        time.sleep(0.8)
        print("-------INÍCIO DA HISTÓRIA-------")
        time.sleep(0.8)
        self.digitar("\nVocê desperta com a cabeça latejando em uma caverna úmida e parcialmente iluminada...")
        time.sleep(1)
        self.digitar("\nO silêncio é quebrado apenas pelo eco distante de gotas caindo...")
        time.sleep(1)
        self.digitar("\nÀ sua esquerda, uma porta antiga e desgastada parece guardar segredos esquecidos...")
        time.sleep(1)
        self.digitar("\nÀ sua direita, uma passagem estreita se estende pela escuridão, convidando — ou ameaçando — quem ousar seguir adiante...")
        time.sleep(1)
        print("\n\n1 - Porta Antiga  2 - Passagem Estreita")
        time.sleep(1)
        escolherPassagem = input("\nQual será o seu próximo passo? ")    
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

        