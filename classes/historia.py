import time
import os
from .personagens import Inimigo
from classes.batalha import Batalha
import questionary


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

        self.digitar("Você se aproxima da porta antiga com cautela, pousa a mão sobre a madeira desgastada e tenta, de alguma forma, forçar sua abertura..." \
        "\nAo entrar na sala, você se depara, ao fundo, com uma figura de estatura média que se destaca na penumbra..." \
        "\nSua pele esverdeada reflete a pouca luz, e em uma das mãos ela segura uma lâmina curta e gasta..." \
        "\nÀ medida que você se aproxima, a criatura se move — é um goblin..." \
        "\nO goblin solta um rosnado baixo, assume uma postura agressiva e ergue a arma..." \
        "\nVocê se prepara para o combate.")

        time.sleep(2)

        # Batalha       
        Goblin = Inimigo(30, 10, 12, "GOBLIN")
        Batalhar = Batalha(self.jogador, Goblin)
        Batalhar.combate(self.jogador, Goblin, self.jogador.arma_escolhida.dano, Goblin.dano, self.jogador.defesa, Goblin.defesa)
        time.sleep(2)
        os.system('cls')

        self.digitar("Após derrotar o goblin e recuperar o fôlego, você percebe dois túneis ao fundo da sala..." \
        "\nUm segue para a esquerda, o outro para a direita..." \
        "\n 1 - Túnel da esquerda  2 - Túnel da direita")
        print("\n\nQual será o seu próximo passo? ")

        escolherTunel = questionary.select(
            "Qual será o seu próximo passo?",
            choices=[
                "1",
                "2"
            ]).ask()


        self.digitar("...", 1)
        time.sleep(0.8)

        match escolherTunel:
            case "1":
                os.system('cls')
                self.digitar("\nVocê decide seguir pelo túnel da esquerda e logo percebe que ele é muito mais longo do que imaginava..." \
                "\nAo final do caminho, você chega a uma grande sala surpreendentemente arrumada..." \
                "\nEnquanto avança pelo salão, seus olhos são atraídos por uma estrutura rudimentar que lembra um trono..." \
                "\nSentado sobre ele está uma criatura de quase dois metros de altura, com músculos enormes e empunhando uma enorme espada..." \
                "\nA verdade se revela quando você observa com mais atenção: você acaba de encontrar um orc..." \
                "\nVocê se prepara para o combate.")
                time.sleep(2)

                #Batalha
                Orc = Inimigo(67, 12, 18, "ORC")
                Batalhar = Batalha(self.jogador, Orc)
                Batalhar.combate(self.jogador, Orc, self.jogador.arma_escolhida.dano, Orc.dano, self.jogador.defesa, Orc.defesa)
                time.sleep(2)
                os.system('cls')

            case "2":
                os.system('cls')
                self.digitar("\nVocê decide seguir pelo túnel da direita e logo percebe que ele é muito mais longo do que imaginava..." \
                "\nAo final do túnel, você se depara com um grande salão iluminado por tochas tremulantes..." \
                "\nNo centro do salão repousa uma criatura humanoide de grande porte, de pele acinzentada e aparência brutal..." \
                "\nConforme você avança em sua direção, percebe seus movimentos desajeitados e o olhar vazio..." \
                "\n Não há mais dúvidas: a criatura à sua frente é um troll." \
                "\nVocê se prepara para o combate.")
                time.sleep(2)

                #Batalha
                Troll = Inimigo(84, 14, 12, "TROLL")
                Batalhar = Batalha(self.jogador, Troll)
                Batalhar.combate(self.jogador, Troll, self.jogador.arma_escolhida.dano, Troll.dano, self.jogador.defesa, Troll.defesa)
                time.sleep(2)
                os.system('cls')
                
            

    # Fluxo de escolha caminho estreito
    def _escolherCaminhoEstreito(self):
        os.system('cls')
        self.digitar("\nVocê se dirige até a passagem estreita com cautela, atento a cada som ao seu redor..." \
        "\nAo atravessar a passagem, você se depara com uma silhueta inquietante: um réptil humanoide..." \
        "\ntrajando uma armadura de couro gasta e empunhando um pequeno machado. Os segundos se..." \
        "\narrastam enquanto sua visão se ajusta à penumbra… então a verdade se revela. A criatura à sua frente é um kobold..." \
        "\nO kobold percebe sua presença e, sem hesitar, assume uma postura de combate..." \
        "\nVocê se prepara para o combate.")
        time.sleep(2)
        os.system('cls')

        #Batalha
        Kobold = Inimigo(34, 10, 12, "KOBOLD")
        Batalhar = Batalha(self.jogador, Kobold)
        Batalhar.combate(self.jogador, Kobold, self.jogador.arma_escolhida.dano, Kobold.dano, self.jogador.defesa, Kobold.defesa)
        time.sleep(2)
        os.system('cls')

        self.digitar("Após derrotar o kobold e recuperar o fôlego, você percebe dois túneis ao fundo da sala..." \
        "\nUm segue para a esquerda, o outro para a direita..." \
        "\n 1 - Túnel da esquerda  2 - Túnel da direita")
        escolherTunel = input("\n\nQual será o seu próximo passo? ")
        self.digitar("...", 1)
        time.sleep(0.8)

        match escolherTunel:
            case "1":
                os.system('cls')
                self.digitar("\nVocê decide seguir pelo túnel da esquerda e logo percebe que ele é muito mais longo do que imaginava..." \
                "\nAo final do caminho, você chega a uma grande sala surpreendentemente arrumada..." \
                "\nEnquanto avança pelo salão, seus olhos são atraídos por uma estrutura rudimentar que lembra um trono..." \
                "\nSentado sobre ele está uma criatura de quase dois metros de altura, com músculos enormes e empunhando uma enorme espada..." \
                "\nA verdade se revela quando você observa com mais atenção: você acaba de encontrar um orc..." \
                "\nVocê se prepara para o combate.")
                time.sleep(2)

                #Batalha
                Orc = Inimigo(67, 12, 18, "ORC")
                Batalhar = Batalha(self.jogador, Orc)
                Batalhar.combate(self.jogador, Orc, self.jogador.arma_escolhida.dano, Orc.dano, self.jogador.defesa, Orc.defesa)
                time.sleep(2)
                os.system('cls')

            case "2":
                os.system('cls')
                self.digitar("\nVocê decide seguir pelo túnel da direita e logo percebe que ele é muito mais longo do que imaginava..." \
                "\nAo final do túnel, você se depara com um grande salão iluminado por tochas tremulantes..." \
                "\nNo centro do salão repousa uma criatura humanoide de grande porte, de pele acinzentada e aparência brutal..." \
                "\nConforme você avança em sua direção, percebe seus movimentos desajeitados e o olhar vazio..." \
                "\n Não há mais dúvidas: a criatura à sua frente é um troll." \
                "\nVocê se prepara para o combate.")
                time.sleep(2)

                #Batalha
                Troll = Inimigo(84, 14, 12, "TROLL")
                Batalhar = Batalha(self.jogador, Troll)
                Batalhar.combate(self.jogador, Troll, self.jogador.arma_escolhida.dano, Troll.dano, self.jogador.defesa, Troll.defesa)
                time.sleep(2)
                os.system('cls')
        ####

        # outroinimifo = Inimigo(1, 2, 8, "OUTRO INIMIGO")
        # Batalhar = Batalha(self.jogador, outroinimifo)
        # Batalhar.combate(self.jogador, outroinimifo, self.jogador.arma_escolhida.dano, outroinimifo.dano, self.jogador.defesa, outroinimifo.defesa)

        
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
            case _:
                while True:
                    comando = input("\nEscolha uma alternativa válida: ")
                    if comando == "1" or comando == "2":
                        break

        