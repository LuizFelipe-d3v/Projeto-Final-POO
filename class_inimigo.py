class Inimigo:
    def __init__(self, nome, dano, arma, vida, defesa):
        self.nome = nome
        self.__dano = dano
        self.nome = arma
        self.__vida = vida
        self.__defesa = defesa

    def get_dano(self):
        return self.__dano
    
    def get_vida(self):
        return self.__vida
    
    def get_defesa(self):
        return self.__defesa