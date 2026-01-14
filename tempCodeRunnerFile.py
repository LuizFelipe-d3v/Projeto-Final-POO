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

        lista_armas = [Cajado, Varinha]

        Mago = Personagem("Mago", 10, lista_armas, 14)
        print("Você escolheu a classe Mago! \nEscolha sua arma: ")
        print("")

        print("")
        print("Aqui estao seus status: ")
        print(f"Vida: {Mago.vida}")
        print(f"Defesa: {Mago.defesa}")
        print("")
        print("---------EQUIPAMENTOS-----------")
        i = 1
        for arma in lista_armas:
            print(f"{i} - Nome: {arma.nome} - Dano: {arma.dano}")
            i = i + 1
        

        print("")
        arma_escolhida = input("Faça sua escolha: ")

        match arma_escolhida:
            case "1":
                Mago.arma_escolhida = lista_armas[0]
                print(f"Voce escolheu: {Mago.arma_escolhida.nome}")
            case "2":
                Mago.arma_escolhida = lista_armas[1]
                print(f"Voce escolheu: {Mago.arma_escolhida.nome}")


        # print("")
        # print("Aqui estao seus status: ")
        # print(f"Vida: {Mago.vida}")
        # print(f"Defesa: {Mago.defesa}")
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")
    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")
    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")



    