import os
class Personagem:
    def __init__(self, vida=None, defesa=None):
        self.vida = vida
        self.defesa = defesa
    
    def estar_vivo(self):
        return self.vida > 0
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        
        print(f"Vida restante: {self.vida}")
    
    def atacar(self, alvo, dano):
        alvo.receber_dano(dano)
                   
class Jogador(Personagem):
    def __init__(self, classe=None, vida=None, armas=None, defesa=None, arma_escolhida=None):
        super().__init__(vida, defesa)
        self.classe = classe
        self.armas = armas
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
    
    def atacar(self, alvo):
        dano = self.arma_escolhida.dano
        super().atacar(alvo, dano)
    
    def receber_dano(self, dano):
        return super().receber_dano(dano)
    
    def estar_vivo(self):
        return super().estar_vivo()

class Inimigo(Personagem):
    def __init__(self, vida=None, defesa=None, dano=None, nome=None):
        super().__init__(vida, defesa)
        self.dano = dano
        self.nome = nome
    
    def atacar(self, alvo):
        super().atacar(alvo, self.dano)
    
    def receber_dano(self, dano):
        return super().receber_dano(dano)
    
    def estar_vivo(self):
        return super().estar_vivo()
        