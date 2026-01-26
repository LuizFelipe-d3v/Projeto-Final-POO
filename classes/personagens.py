import os
from classes.itens import Arma, Pocao
from abc import ABC, abstractmethod
import questionary


class Personagem(ABC):
    
    def __init__(self, vida=None, defesa=None, armas=None, habilidades=None):
        self.__vida = vida
        self.__defesa = defesa
        self.__vida_maxima = vida    
    
    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        self.__vida = valor

        if self.__vida < 0:
            self.__vida = 0

        if self.__vida > self.__vida_maxima:
            self.__vida = self.__vida_maxima

    @property
    def defesa(self):
        return self.__defesa

    def estar_vivo(self):
        return self.__vida > 0
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
        
        print(f"Vida restante: {self.vida}")
    
    @abstractmethod
    def atacar(self, alvo, dano):
        pass
                   
class Jogador(Personagem):
    def __init__(self, classe=None, vida=None, inventario=[], armas=None, defesa=None, arma_escolhida=None, habilidades=None, mana=None):
        super().__init__(vida, defesa)
        self.__mana = mana
        self.__mana_maxima = mana
        self.classe = classe
        #self.armas = armas
        self.arma_escolhida = arma_escolhida
        self.inventario = inventario
        self.habilidades = habilidades

    @property
    def mana_maxima(self):
        return self.__mana_maxima

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, valor):
        self.__mana = valor

        if self.__mana < 0:
            self.__mana = 0

        if self.__mana > self.__mana_maxima:
            self.__mana = self.__mana_maxima

    def apresentar(self):
        print("\n------------STATUS------------")
        print(f"Vida: {self.vida}")
        print(f"Defesa: {self.defesa}")
        questionary.text("ESTÁ PRONTO PARA ESCOLHER SEU EQUIPAMENTO? (aperte Enter para seguir)").ask()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # def escolher_arma(self):
    #     opcoes = []

    #     for arma in self.armas:
    #         texto_opcao = f"{arma.nome} (Dano: {arma.dano})"
    #         opcoes.append(texto_opcao)

    #     escolha = questionary.select(
    #         "Escolha sua arma:",
    #         choices=opcoes
    #     ).ask()

    #     indice = opcoes.index(escolha)
    #     self.arma_escolhida = self.armas[indice]
    #     print(f"\nVocê escolheu: {self.arma_escolhida.nome}")


    def usar_habilidade(self, habilidade, inimigo):
        sucesso = habilidade.executar(self, inimigo)
        if sucesso:
            print(f"\nVocê usou a habilidade {habilidade.nome} causando {habilidade.dano} de dano!")
        else:
            print("\nMana insuficiente para usar a habilidade.")
    
    def receber_dano(self, dano):
        print("\nVocê foi atingido!")
        return super().receber_dano(dano)
    
    def atacar(self, alvo):
        dano = self.arma_escolhida.dano
        super().atacar(alvo, dano)

    def guardar_item(self, item):
        self.inventario.append(item)
        print(f"\nVocê guardou {item.nome} no inventário.")

    def mostrar_inventario(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n------------INVENTÁRIO------------")
            print(f"Vida: {self.vida}/{self.vida_maxima}")
            if hasattr(self, 'mana'):
                print(f"Mana: {self.mana}/{self.mana_maxima}")
            
            if self.arma_escolhida:
                print(f"Arma equipada: {self.arma_escolhida.nome} (Dano: {self.arma_escolhida.dano})")

            opcoes = []
            for item in self.inventario:
                opcoes.append(questionary.Choice(item.nome, value=item))
            
            opcoes.append(questionary.Choice("Voltar", value="voltar"))

            escolha = questionary.select(
                "Escolha um item para usar ou 'Voltar' para sair:",
                choices=opcoes
            ).ask()

            if escolha == "voltar" or escolha is None:
                break
            
            item = escolha
            if isinstance(item, Pocao):
                item.usar(self)
                self.inventario.remove(item)
            elif isinstance(item, Arma):
                item.usar(self)
            
            questionary.text("\nPressione Enter para continuar...").ask()
    
class Inimigo(Personagem):
    def __init__(self, vida=None, defesa=None, dano=None, nome=None):
        super().__init__(vida, defesa)
        self.dano = dano
        self.nome = nome
    
    def atacar(self, alvo):
        print(f"\nO {self.nome} avança para atacar!")
        alvo.receber_dano(self.dano)
    
    def receber_dano(self, dano):
        print(f"O inimigo {self.nome} foi atingido!")
        super().receber_dano(dano)
    
class Habilidade:
    def __init__(self, nome: str, descricao: str, dano: int, custo_mana: int):
        self.nome = nome
        self.descricao = descricao
        self.dano = dano
        self.custo_mana = custo_mana

    def pode_usar(self, jogador) -> bool:
        return jogador.mana >= self.custo_mana

    def executar(self, jogador, inimigo):
        if self.pode_usar(jogador):
            jogador.mana -= self.custo_mana
            inimigo.receber_dano(self.dano)
            return True
        return False 
        