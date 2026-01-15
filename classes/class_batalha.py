# from class_personagem import Personagem
# from class_inimigo import Inimigo
import random

class Batalha:
    def __init__(self, jogador1, jogador2): 
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def combate(self, personagem, inimigo, dano_personagem, dano_inimigo, defesa_personagem, defesa_inimigo):
        print("A BATALHA COMEÇOU")
        numero = random.randint(1, 20)
        

    # def inimigo_bater(self, dano_inimigo, vida, defesa):
    #    print("A BATALHA COMEÇOU")
    #    print("O INIMIGO VAI ATACAR")
    #    numero = random.randint(1, 20)
    #    print(f"dano do inimigo - {dano_inimigo} vida do personagem - {vida} defesa do personagem - {defesa}")
    #    print(numero)
    #    if numero >= defesa:
    #        vida = vida - dano_inimigo 
    #        print(f"VIDA RESTANTE = {vida}")
    #    else:
    #        print("O INIMIGO ERROU O GOLPE")
    #        print(numero)

    # def personagem_bater(self):
    #     numero = random.randint(1, 20)
    #     print(f"dano do inimigo - {dano_inimigo} vida do personagem - {vida} defesa do personagem - {defesa}")
    #     print(numero)
    #    if numero >= defesa:
    #        vida = vida - dano_inimigo 
    #        print(f"VIDA RESTANTE = {vida}")
    #    else:
    #        print("O INIMIGO ERROU O GOLPE")
    #        print(numero)


    numero = random.randint(1, 20)
    print(numero)