import os
from abc import ABC, abstractmethod
import questionary

class Personagem(ABC):
    """
    Classe abstrata que serve como base para jogadores e inimigos do jogo.
    Define os atributos básicos de vida e defesa.
    """
    def __init__(self, vida=None, defesa=None):
        self._vida = vida          
        self._defesa = defesa      
        self._vida_maxima = vida   
    
    @property
    def vida_maxima(self):
        return self._vida_maxima

    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        self._vida = valor
        if self._vida < 0:
            self._vida = 0
        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

    @property
    def defesa(self):
        return self._defesa

    def estar_vivo(self):
        return self._vida > 0
    
    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"\nVida restante: {self.vida}\n")
    
    @abstractmethod
    def atacar(self, alvo, dano):
        pass

class Jogador(Personagem):
    def __init__(self, classe=None, vida=None, inventario=[], defesa=None, arma_escolhida=None, dados_habilidades=None, mana=None, progresso_historia="inicio"):
        super().__init__(vida, defesa)
        self._mana = mana                
        self._mana_maxima = mana         
        self.classe = classe
        self.arma_escolhida = arma_escolhida
        self.inventario = inventario
        self.habilidade = None
        self.progresso_historia = progresso_historia
        if dados_habilidades:
            self.habilidade = Habilidade(
                dados_habilidades['nome'],
                dados_habilidades['descricao'],
                dados_habilidades['dano'],
                dados_habilidades['custo_mana']
            )

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor
        if self._vida < 0: self._vida = 0
        if self._vida > self._vida_maxima: self._vida = self._vida_maxima
        
        if not self.estar_vivo():
            self.habilidade = None

    @property
    def mana_maxima(self):
        return self._mana_maxima

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        self._mana = valor
        if self._mana < 0:
            self._mana = 0
        if self._mana > self._mana_maxima:
            self._mana = self._mana_maxima

    def apresentar(self):
        print("\n------------STATUS------------")
        print(f"Vida: {self.vida}/{self.vida_maxima}")
        print(f"Defesa: {self.defesa}")
        print(f"Mana: {self.mana}/{self.mana_maxima}\n")
        questionary.text("\nESTÁ PRONTO PARA ESCOLHER SEU EQUIPAMENTO? (aperte Enter para seguir)",qmark="").ask()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def usar_habilidade(self, inimigo):
        
        sucesso = self.habilidade.executar(self, inimigo)
        if sucesso:
            print(f"\nVocê usou a habilidade {self.habilidade.nome} causando {self.habilidade.dano} de dano!")
            return True
        else:
            print("\nMana insuficiente para usar a habilidade.")
            return False

    def receber_dano(self, dano):
        print("\nVocê foi atingido!")
        return super().receber_dano(dano)
    
    def atacar(self, alvo):
        dano = self.arma_escolhida.dano
        super().atacar(alvo, dano)

    def mostrar_inventario(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n------------INVENTÁRIO------------")
            print(f"Vida: {self.vida}/{self.vida_maxima}")
            print(f"Mana: {self.mana}/{self.mana_maxima}")
            print(f"Habilidade especial: {self.habilidade.nome} (Dano: {self.habilidade.dano}, Custo de Mana: {self.habilidade.custo_mana})\n")

            if self.arma_escolhida:
                print(f"Arma equipada: {self.arma_escolhida.nome} (Dano: {self.arma_escolhida.dano})")

            opcoes = []
            for item in self.inventario:
                opcoes.append(questionary.Choice(item.nome, value=item))
            
            opcoes.append(questionary.Choice("🔙 Voltar", value="voltar"))

            escolha = questionary.select(
                "\nEscolha um item para usar ou 'Voltar' para sair:",
                choices=opcoes,
                qmark=""
   
            ).ask()

            if escolha == "voltar" or escolha is None:
                return False
            
            item = escolha
            item.usar(self)
            
            questionary.text("\nPressione Enter para continuar...",qmark="").ask()
            return True

class Inimigo(Personagem):
    """
    Representa criaturas hostis que o jogador enfrenta durante a aventura.
    """
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
    """
    Define um ataque especial que consome mana.
    """
    def __init__(self, nome: str, descricao: str, dano: int, custo_mana: int):
        self.nome = nome
        self.descricao = descricao
        self.dano = dano
        self.custo_mana = custo_mana

    def pode_usar(self, jogador):
        return jogador.mana >= self.custo_mana

    def executar(self, jogador, inimigo):
        if self.pode_usar(jogador):
            jogador.mana -= self.custo_mana
            inimigo.receber_dano(self.dano)
            return True
        return False