import os
from abc import ABC, abstractmethod
import questionary


class Personagem(ABC):
    
    def __init__(self, vida=None, defesa=None, armas=None, habilidades=None):
        self._vida = vida
        self._defesa = defesa
        self._vida_maxima = vida    
    
    @property
    def vida_maxima(self):
        return self._vida_maxima

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        self._vida += valor

        if self._vida < 0:
            self._vida = 0

        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

    @property
    def defesa(self):
        return self.__defesa

    def estar_vivo(self):
        return self._vida > 0
    
    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        
        print(f"Vida restante: {self.vida}")
    
    @abstractmethod
    def atacar(self, alvo, dano):
        pass
                   
class Jogador(Personagem):
    def __init__(self, classe=None, vida=None, armas=None, defesa=None, arma_escolhida=None, habilidades=None, mana=None):
        super().__init__(vida, defesa)
        self.__mana = mana
        self.__mana_maxima = mana
        self.classe = classe
        self.armas = armas
        self.arma_escolhida = arma_escolhida
        self.inventario = []
        self.habilidades = habilidades

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, valor):
        self.__mana += valor

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
        
    def escolher_arma(self):
        opcoes = []

        for arma in self.armas:
            texto_opcao = f"{arma.nome} (Dano: {arma.dano})"
            opcoes.append(texto_opcao)

        escolha = questionary.select(
            "Escolha sua arma:",
            choices=opcoes
        ).ask()

        indice = opcoes.index(escolha)
        self.arma_escolhida = self.armas[indice]
        print(f"\nVocê escolheu: {self.arma_escolhida.nome}")


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
        