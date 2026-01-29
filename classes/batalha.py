import time
import random
import os
from classes.personagens import Jogador, Inimigo
import questionary

# Gerencia o fluxo lógico de um confronto por turnos entre Jogador e Inimigo.
class Batalha:
    """
    Classe responsável por mediar o combate por turnos entre o Jogador e um Inimigo.
    """
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def combate(self):
        """Executa o loop principal de combate até que alguém seja derrotado."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n-------- PREPARE-SE A BATALHA IRÁ COMEÇAR! --------")
        time.sleep(1)

        while self.jogador.estar_vivo() and self.inimigo.estar_vivo():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- STATUS DO COMBATE ---")
            print(f" {self.jogador.classe}: {self.jogador.vida}/{self.jogador.vida_maxima} HP | Mana: {self.jogador.mana}/{self.jogador.mana_maxima}")
            print(f" {self.inimigo.nome}: {self.inimigo.vida} HP")
            print("-" * 25)

            escolha = questionary.select(
                "Escolha sua ação:",
                choices=[
                    "Atacar",
                    "Usar Habilidade Especial",
                    "Abrir Inventário",
                ],
                qmark=""
            ).ask()

            if escolha == "Atacar":
                self.turno_jogador_ataque()
            
            elif escolha == "Usar Habilidade Especial":
                if not self.turno_jogador_habilidade():
                    continue
            
            elif escolha == "Abrir Inventário":
                usou_item = self.jogador.mostrar_inventario()
                if not usou_item:
                    continue

            if not self.inimigo.estar_vivo():
                print("\nO inimigo foi derrotado!")
                time.sleep(2)
                break

            self.turno_inimigo()

            if not self.jogador.estar_vivo():
                print("\nVocê foi derrotado!")
                time.sleep(2)
                break

        print("\n-------- FIM DA BATALHA --------")
            
    def turno_jogador_ataque(self):
        """Executa a lógica de ataque físico do jogador, incluindo rolagem de dados e acerto crítico."""
        print("\nROLANDO DADOS DE ATAQUE...")
        time.sleep(0.8)
        dado = random.randint(1, 20)
        print(f"Resultado: {dado}")

        if dado >= self.inimigo.defesa:
            dano = self.jogador.arma_escolhida.dano
            if dado == 20:
                print(" ACERTO CRÍTICO!")
                dano *= 2
            
            print(f"Você causou {dano} de dano ao {self.inimigo.nome}!")
            self.inimigo.receber_dano(dano)
        else:
            print(f"🛡️ O {self.inimigo.nome} bloqueou seu ataque!")
        
        time.sleep(1.5)

        questionary.text("\nPressione Enter para continuar...",qmark="").ask()


    def turno_jogador_habilidade(self):
        """Gerencia a escolha e execução de habilidades especiais durante o combate."""
        
        habilidade = self.jogador.habilidade
        print(f"\nDeseja usar {habilidade.nome}?")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Dano: {habilidade.dano} | ✨ Custo: {habilidade.custo_mana} mana")

        confirmar = questionary.confirm(f"Confirmar uso de {habilidade.nome}?").ask()
        
        if confirmar:
            if self.jogador.habilidade.pode_usar(self.jogador):
                self.jogador.usar_habilidade(self.inimigo)
                time.sleep(1.5)
                return True
            else:
                print("\nMana insuficiente")
                time.sleep(1.2)
                return False
        return False 

        questionary.text("\nPressione Enter para continuar...",qmark="").ask()

    def turno_inimigo(self):
        """Executa o turno do inimigo, calculando o ataque contra o jogador."""
        print(f"\nTURNO DO {self.inimigo.nome}...")
        time.sleep(1)
        dado = random.randint(1, 20)
        
        if dado >= self.jogador.defesa:
            print(f"O {self.inimigo.nome} acertou")
            self.jogador.receber_dano(self.inimigo.dano)
        else:
            print(f"você se esquivou do ataque do {self.inimigo.nome}!")
        
        time.sleep(1.5)

        questionary.text("\nPressione Enter para continuar...",qmark="").ask()

