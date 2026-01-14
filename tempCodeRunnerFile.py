# Inicio do projeto 
import os
from class_arma import Arma
from class_personagem import Personagem

print("-----------------")  
print("BEM VINDO AO JOGO")  
print("-----------------")  
print("")
print("ESCOLHA SUA CLASSE:")
print("1 - Mago")
print("2 - Assasino")
print("3 - Tank")
print("4 - Paladino")
print("5 - Barbaro")
print("")
classe = input("Faça sua escolha: ")
os.system('cls')

match classe:
    case "1": 
        Cajado = Arma("Cajado", 4)
        Varinha = Arma("Varinha", 3)

        lista_armas_mago = [Cajado, Varinha]

        Mago = Personagem("Mago", 10, lista_armas_mago, 14)
        print("Você escolheu a classe Mago!")
        print("")
        print("Aqui estao seus status: ")
        print(f"Vida: {Mago.vida}")
        print(f"Defesa: {Mago.defesa}")
        print(f"Essas sao suas armas disponiveis: {Cajado.nome} e {Varinha.nome}")
        print("")
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in lista_armas_mago:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1       

        print("")
        arma_escolhida = input("Faça sua escolha: ")

        match arma_escolhida:
            case "1":
                Mago.arma_escolhida = lista_armas_mago[0]
                print(f"Voce escolheu: {Mago.arma_escolhida.nome}")
            case "2":
                Mago.arma_escolhida = lista_armas_mago[1]
                print(f"Voce escolheu: {Mago.arma_escolhida.nome}")


        # print("")
        # print("Aqui estao seus status: ")
        # print(f"Vida: {Mago.vida}")
        # print(f"Defesa: {Mago.defesa}")
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")
        Adagas = Arma("Adaga", 4)
        Rapiera = Arma("Rapiera", 3)

        lista_armas_assasino = [Adagas, Rapiera]

        Assasino = Personagem("Assasino", 14, lista_armas_assasino, 16)
        print("Você escolheu a classe Assasino!")
        print("")
        print("")
        print("Aqui estao seus status: ")
        print(f"Vida: {Assasino.vida}")
        print(f"Defesa: {Assasino.defesa}")
        print(f"Essas sao suas armas disponiveis: {Adagas.nome} e {Rapiera.nome}")
        print("")
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in lista_armas_assasino:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1       

        print("")
        arma_escolhida = input("Faça sua escolha: ")

        match arma_escolhida:
            case "1":
                Assasino.arma_escolhida = lista_armas_assasino[0]
                print(f"Voce escolheu: {Assasino.arma_escolhida.nome}")
            case "2":
                Assasino.arma_escolhida = lista_armas_assasino[1]
                print(f"Voce escolheu: {Assasino.arma_escolhida.nome}")
    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")
        Manoplas = Arma("Manoplas", 10)
        Escudo = Arma("Escudo", 6)

        lista_armas_tank = [Manoplas, Escudo]

        Tank = Personagem("Tank", 30, lista_armas_tank, 19)
        print("Você escolheu a classe Tank!")
        print("")
        print("")
        print("Aqui estao seus status: ")
        print(f"Vida: {Tank.vida}")
        print(f"Defesa: {Tank.defesa}")
        print(f"Essas sao suas armas disponiveis: {Manoplas.nome} e {Escudo.nome}")
        print("")
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in lista_armas_tank:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1       

        print("")
        arma_escolhida = input("Faça sua escolha: ")

        match arma_escolhida:
            case "1":
                Tank.arma_escolhida = lista_armas_tank[0]
                print(f"Voce escolheu: {Tank.arma_escolhida.nome}")
            case "2":
                Tank.arma_escolhida = lista_armas_tank[1]
                print(f"Voce escolheu: {Tank.arma_escolhida.nome}")
    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")
        Espada_Longa = Arma("Espada Longa", 4)
        Alabarda = Arma("Alabarda", 3)

        lista_armas_paladino = [Espada_Longa, Alabarda]

        Paladino = Personagem("Paladino", 24, lista_armas_paladino, 17)
        print("Você escolheu a classe Paladino!")
        print("")
        print("")
        print("Aqui estao seus status: ")
        print(f"Vida: {Paladino.vida}")
        print(f"Defesa: {Paladino.defesa}")
        print(f"Essas sao suas armas disponiveis: {Espada_Longa.nome} e {Alabarda.nome}")
        print("")
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in lista_armas_paladino:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1       

        print("")
        arma_escolhida = input("Faça sua escolha: ")

        match arma_escolhida:
            case "1":
                Paladino.arma_escolhida = lista_armas_paladino[0]
                print(f"Voce escolheu: {Paladino.arma_escolhida.nome}")
            case "2":
                Paladino.arma_escolhida = lista_armas_paladino[1]
                print(f"Voce escolheu: {Paladino.arma_escolhida.nome}")
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")
