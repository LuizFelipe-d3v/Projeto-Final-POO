# Inicio do projeto 
import os
import questionary
from questionary import Choice
from classes.itens import Arma, Pocao
from classes.personagens import Jogador, Habilidade
from classes.historia import Historia


classe = questionary.select(
    "Escolha sua classe:",
    choices=[
        Choice("🧙  Mago", value="1"),
        Choice("🗡️  Assassino", value="2"),
        Choice("🛡️  Tank", value="3"),
        Choice("⚔️  Paladino", value="4"),
        Choice("🔥  Bárbaro", value="5"),
    ]
).ask()


if classe is None:
    print("Escolha cancelada. Saindo do jogo...")
    exit()


os.system('cls' if os.name == 'nt' else 'clear')

personagem_escolhido = Jogador()


match classe:
    case "1": 
        print("Você escolheu a classe Mago!")

        Cajado = Arma("Cajado", 4)
        Varinha = Arma("Varinha", 3)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        habilidades_mago = {"nome": "bola de fogo", "descricao": "uma grande bola de fogo", "valor": 5, "custo_mana": 10}
        #trocar para iventario
        inventario = [Varinha, Cajado, pocao_vida, pocao_mana]
        # Ordem: classe, vida, inventario, armas, defesa, arma_escolhida, habilidades, mana
        personagem_escolhido = Jogador("Mago", 100, inventario, 8, None, habilidades_mago, 50)
        personagem_escolhido.apresentar()   
        print ("Escolha sua arma inicial:")
        personagem_escolhido.mostrar_inventario()
                 
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")

        Adagas = Arma("Adaga", 4)
        Rapiera = Arma("Rapiera", 3)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        inventario = [Adagas, Rapiera, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Assassino", 100, inventario, 16, None, 40)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")

        Manoplas = Arma("Manoplas", 10)
        Escudo = Arma("Escudo", 6)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        inventario = [Manoplas, Escudo, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Tank", 150, inventario, 30, None, 20)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")

        Espada_Longa = Arma("Espada Longa", 4)
        Alabarda = Arma("Alabarda", 3)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        inventario = [Espada_Longa, Alabarda, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Paladino", 120, inventario, 20, None, 30)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")

        Machado = Arma("Machado", 18)
        Lanca = Arma("Lança", 6)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        inventario = [Machado, Lanca, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Bárbaro", 130, inventario, 15, None, 10)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()

# História
# historia = Historia(personagem_escolhido)   
# historia.iniciarHistoria()

# Batalha       
# Mau = Inimigo(15, 10, 10, "GOBLIM")
# Batalhar = Batalha(personagem_escolhido, Mau)

# Batalhar.combate(personagem_escolhido, Mau, personagem_escolhido.arma_escolhida.dano, Mau.dano, personagem_escolhido.defesa, Mau.defesa)