from abc import ABC
class IItem(ABC):
    """Interface base para definição de comportamentos de itens."""
    def __init__(self, nome):
        self.nome = nome    
    
    def usar(self, usuario):
        pass
class Arma(IItem):
    """Item do tipo arma que aumenta o dano do portador."""
    def __init__(self, nome, dano):
        super().__init__(nome)
        self.__dano = dano
        self.categoria = "arma"

    @property
    def dano(self):
        return self.__dano
    
    def usar(self, usuario):
        usuario.arma_escolhida = self
        print(f"{usuario.__class__.__name__} equipou a arma: {self.nome}")

class Pocao(IItem):
    """Consumível utilizado para restaurar atributos como Vida ou Mana."""
    def __init__(self, nome, valor_recuperacao, tipo):
        super().__init__(nome)
        self.__valor_recuperacao = valor_recuperacao
        self.tipo = tipo
        self.categoria = "pocao"
    
    @property
    def valor_recuperacao(self):
        return self.__valor_recuperacao

    def usar(self, usuario):
        if self.tipo == "vida":
            usuario.vida += self.__valor_recuperacao
            
            print(f"{usuario.__class__.__name__} usou {self.nome} e recuperou {self.__valor_recuperacao} de vida.")
            print(f"Vida atual: {usuario.vida}/{usuario.vida_maxima}")

            
        elif self.tipo == "mana":
            usuario.mana += self.__valor_recuperacao
            print(f"{usuario.__class__.__name__} usou {self.nome} e recuperou {self.__valor_recuperacao} de mana.")
            print(f"Mana atual: {usuario.mana}/{usuario.mana_maxima}")
        
        if self in usuario.inventario:
            usuario.inventario.remove(self)