import time
import random

class Batalha:
    def __init__(self, jogador1, jogador2): 
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def combate(self, personagem, inimigo, dano_personagem, dano_inimigo, defesa_personagem, defesa_inimigo):
        print("\n-------- PREPARE-SE A BATALHA IRÁ COMEÇAR! --------")
        time.sleep(2)

        while personagem.estar_vivo() and inimigo.estar_vivo():
            print("\n----------- SEU TURNO -----------")
            time.sleep(0.8)

            blRolarDados = input("Pressione ENTER para rolar os dados.")
            print("ROLANDO OS DADOS...")
            time.sleep(1)
            numero = random.randint(1, 20)
            print(f"Número do ataque: {numero}")
            time.sleep(0.8)

            if numero >= defesa_inimigo:
                print("ATACANDO...")
                time.sleep(0.8)
                print(f"O {inimigo.nome} recebeu {dano_personagem} de dano.")
                inimigo.receber_dano(dano_personagem)
            else:
                print("VOCÊ ERROU O GOLPE")

            time.sleep(1)

            if not inimigo.estar_vivo():
                print(f"\n💀 O {inimigo.nome} FOI DERROTADO!")
                break

            print(f"\n----------- TURNO DO {inimigo.nome} -----------")
            time.sleep(0.8)

            print("ROLANDO OS DADOS...")
            time.sleep(1)
            numero = random.randint(1, 20)
            print(f"Número do ataque: {numero}")
            time.sleep(1)

            if numero >= defesa_personagem:
                print(f"O {inimigo.nome} VAI ATACAR...")
                time.sleep(0.8)
                print(f"Você recebeu {dano_inimigo} de dano.")
                personagem.receber_dano(dano_inimigo)
            else:
                print(f"O {inimigo.nome} ERROU O GOLPE")

            time.sleep(1)

            if not personagem.estar_vivo():
                print("\n☠️ VOCÊ FOI DERROTADO!")
                break
