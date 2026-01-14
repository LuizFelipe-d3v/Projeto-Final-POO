import os

class Personagem:
    def __init__(self, classe, vida, armas, defesa, arma_escolhida=None):
        self.classe = classe
        self.vida = vida
        self.armas = armas
        self.defesa = defesa
        self.arma_escolhida = arma_escolhida
        
    def apresentar(self):
        print("")
        print("------------STATUS------------")
        print(f"Vida: {self.vida}")
        print(f"Defesa: {self.defesa}")
        print("")
        print("ESTÁ PRONTO PARA ESCOLHER SEU EQUIPAMENTO? Aperte qualquer tecla para seguir...")
        n = input("")
        os.system('cls')
        
    def escolher_arma(self):
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in self.armas:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1
        print("")

        arma_escolhida = input("Faça sua escolha: ")
        match arma_escolhida:
            case "1":
                self.arma_escolhida = self.armas[0]
                print(f"Voce escolheu: {self.arma_escolhida.nome}")
            case "2":
                self.arma_escolhida = self.armas[1]
                print(f"Voce escolheu: {self.arma_escolhida.nome}")