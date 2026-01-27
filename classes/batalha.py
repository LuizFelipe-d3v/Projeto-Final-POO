import time
import random
import os
from classes.personagens import Jogador, Inimigo
import questionary

class Batalha:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def combate(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n-------- PREPARE-SE A BATALHA IRÁ COMEÇAR! --------")
        time.sleep(1)

        while self.jogador.estar_vivo() and self.inimigo.estar_vivo():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- STATUS DO COMBATE ---")
            print(f"   {self.jogador.classe}: {self.jogador.vida}/{self.jogador.vida_maxima} HP | Mana: {self.jogador.mana}/{self.jogador.mana_maxima}")
            print(f" {self.inimigo.nome}: {self.inimigo.vida} HP")
            print("-" * 25)

            escolha = questionary.select(
                "Escolha sua ação:",
                choices=[
                    "Atacar",
                    "Usar Habilidade Especial",
                    "Abrir Inventário",
                ]
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
                print("\n O inimigo foi derrotado!")
                time.sleep(2)
                break

            self.turno_inimigo()

            if not self.jogador.estar_vivo():
                print("\n Você foi derrotado!")
                time.sleep(2)
                break

        print("\n-------- FIM DA BATALHA --------")
            


    
    def turno_jogador_ataque(self):
        print("\n ROLANDO DADOS DE ATAQUE...")
        time.sleep(0.8)
        dado = random.randint(1, 20)
        print(f"Resultado: {dado}")

        if dado >= self.inimigo.defesa:
            dano = self.jogador.arma_escolhida.dano
            if dado == 20:
                print(" ACERTO CRÍTICO!")
                dano *= 2
            
            print(f" Você causou {dano} de dano ao {self.inimigo.nome}!")
            self.inimigo.receber_dano(dano)
        else:
            print(f"🛡️  O {self.inimigo.nome} bloqueou seu ataque!")
        
        time.sleep(1.5)

        questionary.text("\nPressione Enter para continuar...").ask()


    def turno_jogador_habilidade(self):
        if not self.jogador.habilidade:
            print(" Você não possui uma habilidade especial para usar!")
            time.sleep(1.5)
            return False

        habilidade = self.jogador.habilidade
        print(f"\n Deseja usar {habilidade.nome}?")
        print(f" Descrição: {habilidade.descricao}")
        print(f" Dano: {habilidade.dano} | ✨ Custo: {habilidade.custo_mana} mana")

        confirmar = questionary.confirm(f"Confirmar uso de {habilidade.nome}?").ask()
        
        if confirmar:
            if self.jogador.mana >= habilidade.custo_mana:
                self.jogador.usar_habilidade(self.inimigo)
                time.sleep(1.5)
                return True
            else:
                print("\nMana insuficiente")
                time.sleep(1.2)
                return False
        return False 

        questionary.text("\nPressione Enter para continuar...").ask()

    def turno_inimigo(self):
        print(f"\n TURNO DO {self.inimigo.nome}...")
        time.sleep(1)
        dado = random.randint(1, 20)
        
        if dado >= self.jogador.defesa:
            print(f"O {self.inimigo.nome} acertou")
            self.jogador.receber_dano(self.inimigo.dano)
        else:
            print(f"você se esquivou do ataque do {self.inimigo.nome}!")
        
        time.sleep(1.5)

        questionary.text("\nPressione Enter para continuar...").ask()

