# Inicio do projeto 
import os
import questionary
from classes.itens import Arma, Pocao
from classes.personagens import Jogador
from classes.historia import Historia
from gerenciar_save import Gerenciar_Save
from questionary import Choice


save = Gerenciar_Save()

dados_salvos = save.carregar()
escolha_inicial = "Novo jogo"

if dados_salvos:
    escolha_inicial = questionary.select(
        "Dados salvos encontrados. O que você gostaria de fazer?",
        choices=[
            Choice("Continuar jogo salvo", value="continuar"),
            Choice("Novo jogo", value="novo_jogo"),
        ]
    ).ask()

personagem_escolhido = None


if escolha_inicial == "continuar":
    itens = []
    for i in dados_salvos["inventario"]:
        if i["tipo"] == "arma":
            itens.append(Arma(i["nome"], i["dano"]))
        else:
            itens.append(Pocao(i["nome"], i["valor"], i["subtipo"]))
    
    personagem_escolhido = Jogador(
        dados_salvos["classe"], 
        dados_salvos["vida"], 
        itens,
        dados_salvos["defesa"], 
        None, 
        None, 
        dados_salvos["mana"],
        dados_salvos["progresso_historia"]
    )
    
    if dados_salvos["classe"] == "Mago":
        personagem_escolhido.habilidade = {"nome": "bola de fogo", "descricao": "uma grande bola de fogo", "dano": 25, "custo_mana": 10}

    elif dados_salvos["classe"] == "Assassino":
        personagem_escolhido.habilidade = {"nome": "ataque furtivo", "descricao": "um ataque mortal vindo das sombras", "dano": 35, "custo_mana": 5}

    elif dados_salvos["classe"] == "Tank":
        personagem_escolhido.habilidade = {"nome": "Impacto do Guardião", "descricao": "avança com o escudo erguido", "dano": 24, "custo_mana": 5}  

    elif dados_salvos["classe"] == "Paladino":
        personagem_escolhido.habilidade = {"nome": "Golpe Sagrado", "descricao": "um ataque abençoado que causa dano extra", "dano": 36, "custo_mana": 8}

    elif dados_salvos["classe"] == "Bárbaro":
        personagem_escolhido.habilidade = {"nome": "Fúria do Berserker", "descricao": "um ataque poderoso que aumenta o dano", "dano": 999, "custo_mana": 0}
        
    if dados_salvos["arma_equipada"]:
        personagem_escolhido.arma_escolhida = Arma(dados_salvos["arma_equipada"]["nome"], dados_salvos["arma_equipada"]["dano"])
    
    print(f"\n[SISTEMA] {personagem_escolhido.classe} carregado com sucesso!")
    classe = "carregado" 

else:
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

if personagem_escolhido is None:
    personagem_escolhido = Jogador()

match classe:
    case "1": 
        print("Você escolheu a classe Mago!")

        Cajado = Arma("Cajado", 16)
        Varinha = Arma("Varinha", 12)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 20, "mana")
        habilidades_mago = {"nome": "bola de fogo", "descricao": "uma grande bola de fogo", "dano": 25, "custo_mana": 10}
        #trocar para iventario
        inventario = [Varinha, Cajado, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Mago", 100, inventario, 15, None, habilidades_mago, 50)
        personagem_escolhido.apresentar()   
        print ("Escolha sua arma inicial:")
        personagem_escolhido.mostrar_inventario()
                 
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")

        Adagas = Arma("Adaga", 18)
        Rapiera = Arma("Rapiera", 20)
        pocao_vida = Pocao("Poção de Vida", 30, "vida")
        pocao_mana = Pocao("Poção de Mana", 10, "mana")
        habilidade_assasino = {"nome": "ataque furtivo", "descricao": "um ataque mortal vindo das sombras", "dano": 35, "custo_mana": 5}
        #trocar para iventario
        inventario = [Adagas, Rapiera, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Assassino", 120, inventario, 16, None, habilidade_assasino, 20)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")

        Manoplas = Arma("Manoplas", 12)
        Escudo = Arma("Escudo", 8)
        pocao_vida = Pocao("Poção de Vida", 50, "vida")
        pocao_mana = Pocao("Poção de Mana", 10, "mana")
        habilidade_tank = {"nome": "Impacto do Guardião", "descricao": "avança com o escudo erguido", "dano": 24, "custo_mana": 5}
        #trocar para iventario
        inventario = [Manoplas, Escudo, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Tank", 150, inventario, 18, None, habilidade_tank, 20)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")

        Espada_Longa = Arma("Espada Longa", 22)
        Alabarda = Arma("Alabarda", 19)
        pocao_vida = Pocao("Poção de Vida", 40, "vida")
        pocao_mana = Pocao("Poção de Mana", 16, "mana")
        habilidade_paladino = {"nome": "Golpe Sagrado", "descricao": "um ataque abençoado que causa dano extra", "dano": 36, "custo_mana": 8}
        #trocar para iventario
        inventario = [Espada_Longa, Alabarda, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Paladino", 120, inventario, 17, None, habilidade_paladino, 20)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")

        Machado = Arma("Machado", 999)
        Lanca = Arma("Lança", 999)
        pocao_vida = Pocao("Poção de Vida", 40, "vida")
        pocao_mana = Pocao("Poção de Mana", 12, "mana")
        habilidade_barbaro = {"nome": "Fúria do Berserker", "descricao": "um ataque poderoso que aumenta o dano", "dano": 999, "custo_mana": 0}
        #trocar para iventario
        inventario = [Machado, Lanca, pocao_vida, pocao_mana]
        personagem_escolhido = Jogador("Bárbaro", 99999, inventario, 21, None, habilidade_barbaro, 999)
        personagem_escolhido.apresentar()
        personagem_escolhido.mostrar_inventario()

# os.system('cls' if os.name == 'nt' else 'clear')
save.salvar(personagem_escolhido)
historia = Historia(personagem_escolhido, save)   
historia.iniciarHistoria()

