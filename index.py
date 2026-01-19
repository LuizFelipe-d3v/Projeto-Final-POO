# Inicio do projeto 
import os
from classes.class_arma import Arma
from classes.class_personagens import Jogador
from classes.class_historia import Historia 

print("-----------------")  
print("BEM VINDO AO JOGO")  
print("-----------------")  
print("\nESCOLHA SUA CLASSE:")
print("1 - Mago")
print("2 - Assasino")
print("3 - Tank")
print("4 - Paladino")
print("5 - Barbaro")
classe = input("\nFaça sua escolha: ")
os.system('cls')

personagem_escolhido = Jogador()

match classe:
    case "1": 
        print("Você escolheu a classe Mago!")

        Cajado = Arma("Cajado", 4)
        Varinha = Arma("Varinha", 3)
        lista_armas_mago = [Cajado, Varinha]

        personagem_escolhido = Jogador("Mago", 100, lista_armas_mago, 8)
        personagem_escolhido.apresentar()       
        personagem_escolhido.escolher_arma()      
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")

        Adagas = Arma("Adaga", 4)
        Rapiera = Arma("Rapiera", 3)
        lista_armas_assasino = [Adagas, Rapiera]

        personagem_escolhido = Jogador("Assasino", 14, lista_armas_assasino, 16)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")

        Manoplas = Arma("Manoplas", 10)
        Escudo = Arma("Escudo", 6)
        lista_armas_tank = [Manoplas, Escudo]

        personagem_escolhido = Jogador("Tank", 30, lista_armas_tank, 19)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")

        Espada_Longa = Arma("Espada Longa", 4)
        Alabarda = Arma("Alabarda", 3)
        lista_armas_paladino = [Espada_Longa, Alabarda]

        personagem_escolhido = Jogador("Paladino", 24, lista_armas_paladino, 17)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")

        Machado = Arma("Machado", 18)
        Lanca = Arma("Lança", 6)
        lista_armas_barbaro = [Machado, Lanca]

        personagem_escolhido = Jogador("Bárbaro", 22, lista_armas_barbaro, 16)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
    case _:
        while True:
            comando = input("\nEscolha uma alternativa válida: ")
            if comando == "1" or comando == "2" or comando == "3" or comando == "4" or comando == "5":
                break

# História
historia = Historia(personagem_escolhido)   
historia.iniciarHistoria()

