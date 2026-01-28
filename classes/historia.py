import time
import os
from .personagens import Inimigo
from classes.batalha import Batalha
import questionary


class Historia:
    def __init__(self, jogador, gerenciador_save=None):
        self.jogador = jogador
        self.save = gerenciador_save

    def digitar(self, texto, velocidade=0.000000000000001):
        for letra in texto:
            print(letra, end='', flush=True)
            if letra == "\n":
                time.sleep(velocidade * 5)
            else:
                time.sleep(velocidade)

    # Fluxo de escolha porta antiga
    def _escolherPortaAntiga(self, pular_batalha=False):
        if not pular_batalha:
            os.system('cls' if os.name == 'nt' else 'clear')

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
            Batalhar.combate()

            self._salvar_progresso("escolha_tunel_porta")

            time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

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
                os.system('cls' if os.name == 'nt' else 'clear')
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
                Batalhar.combate()
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

            case "2":
                os.system('cls' if os.name == 'nt' else 'clear')
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
                Batalhar.combate()
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            

    # Fluxo de escolha caminho estreito
    def _escolherCaminhoEstreito(self, pular_batalha=False):
        if not pular_batalha:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.digitar("\nVocê se dirige até a passagem estreita com cautela, atento a cada som ao seu redor..." \
            "\nAo atravessar a passagem, você se depara com uma silhueta inquietante: um réptil humanoide..." \
            "\ntrajando uma armadura de couro gasta e empunhando um pequeno machado. Os segundos se..." \
            "\narrastam enquanto sua visão se ajusta à penumbra… então a verdade se revela. A criatura à sua frente é um kobold..." \
            "\nO kobold percebe sua presença e, sem hesitar, assume uma postura de combate..." \
            "\nVocê se prepara para o combate.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

            #Batalha
            Kobold = Inimigo(34, 10, 12, "KOBOLD")
            Batalhar = Batalha(self.jogador, Kobold)
            Batalhar.combate()

            self._salvar_progresso("escolha_tunel_estreito")

            time.sleep(2)

        os.system('cls' if os.name == 'nt' else 'clear')

        self.digitar("Após derrotar o kobold e recuperar o fôlego, você percebe dois túneis ao fundo da sala..." \
        "\nUm segue para a esquerda, o outro para a direita..." \
        "\n 1 - Túnel da esquerda  2 - Túnel da direita")
        escolherTunel = input("\n\nQual será o seu próximo passo? ")
        self.digitar("...", 1)
        time.sleep(0.8)

        match escolherTunel:
            case "1":
                os.system('cls' if os.name == 'nt' else 'clear')
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
                Batalhar.combate()
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')

            case "2":
                os.system('cls' if os.name == 'nt' else 'clear')
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
                Batalhar.combate()
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
        ####

        # outroinimifo = Inimigo(1, 2, 8, "OUTRO INIMIGO")
        # Batalhar = Batalha(self.jogador, outroinimifo)
        # Batalhar.combate(self.jogador, outroinimifo, self.jogador.arma_escolhida.dano, outroinimifo.dano, self.jogador.defesa, outroinimifo.defesa)

        
    def iniciarHistoria(self):

        ponto = self.jogador.progresso_historia

        if ponto == "inicio":

            os.system('cls' if os.name == 'nt' else 'clear')
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
                            if comando == "1":
                                self._escolherPortaAntiga()
                            else:
                                self._escolherCaminhoEstreito()
                            break

        elif ponto == "escolha_tunel_porta":
            self._escolherPortaAntiga(pular_batalha=True)
        
        elif ponto == "escolha_tunel_estreito":
            self._escolherCaminhoEstreito(pular_batalha=True)

        elif ponto == "pre_projeto_final":
            pass

        self._salvar_progresso("pre_projeto_final")
            
        self.digitar("\n\nLogo após a árdua batalha, antes mesmo de conseguir recuperar o fôlego, uma passagem secreta se abre silenciosamente bem atrás de você..." \
        "\nEla revela uma verdade inquietante: ainda existe mais um inimigo a ser enfrentado. Ao atravessar o corredor oculto, o ar se torna pesado e um calafrio percorre sua espinha..." \
        "\nDiante de você surge uma presença inacreditavelmente forte e amedrontadora. Não há dúvidas. É ele. O PROJETO FINAL..." \
        "\nA criatura observa cada um de seus movimentos. Você sente o peso do desafio. Reunindo suas últimas energias, ajusta sua postura e prepara sua arma..." \
        "\nSerá que você tem força suficiente para derrotar o PROJETO FINAL e sobreviver ao confronto final?")
        self.digitar("...")

    def _salvar_progresso(self, progresso_nome):
        self.jogador.progresso_historia = progresso_nome
        if self.save:
            self.save.salvar(self.jogador)
                    
        
