# Inicio do projeto 
import os
from classes.class_arma import Arma
from classes.class_personagem import Personagem
from classes.class_inimigo import Inimigo
from classes.class_batalha import Batalha

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

personagem_escolhido = Personagem()


match classe:
    case "1": 
        print("Você escolheu a classe Mago!")

        Cajado = Arma("Cajado", 4)
        Varinha = Arma("Varinha", 3)
        lista_armas_mago = [Cajado, Varinha]

        personagem_escolhido = Personagem("Mago", 100, lista_armas_mago, 8)
        personagem_escolhido.apresentar()       
        personagem_escolhido.escolher_arma()
        
    case "2":
        print("Você escolheu a classe Assasino! A furtividade é sua maior arma.")

        Adagas = Arma("Adaga", 4)
        Rapiera = Arma("Rapiera", 3)
        lista_armas_assasino = [Adagas, Rapiera]

        personagem_escolhido = Personagem("Assasino", 14, lista_armas_assasino, 16)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()

    case "3":
        print("Você escolheu a classe Tank! Sua resistência é imbatível.")

        Manoplas = Arma("Manoplas", 10)
        Escudo = Arma("Escudo", 6)
        lista_armas_tank = [Manoplas, Escudo]

        personagem_escolhido = Personagem("Tank", 30, lista_armas_tank, 19)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()

    case "4":
        print("Você escolheu a classe Paladino! A justiça está do seu lado.")

        Espada_Longa = Arma("Espada Longa", 4)
        Alabarda = Arma("Alabarda", 3)
        lista_armas_paladino = [Espada_Longa, Alabarda]

        personagem_escolhido = Personagem("Paladino", 24, lista_armas_paladino, 17)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
        
    case "5":
        print("Você escolheu a classe Barbaro! A força bruta é sua especialidade.")

        Machado = Arma("Machado", 18)
        Lanca = Arma("Lança", 6)
        lista_armas_barbaro = [Machado, Lanca]

        personagem_escolhido = Personagem("Bárbaro", 22, lista_armas_barbaro, 16)
        personagem_escolhido.apresentar()
        personagem_escolhido.escolher_arma()
        
# Iniciar batalha       
Mau = Inimigo("Mau", 15, "Mão", 25, 10)
Batalhar = Batalha(personagem_escolhido, Mau)

print(Mau.get_dano)
Batalhar.inimigo_bater(Mau.get_dano, personagem_escolhido.vida, personagem_escolhido.defesa)