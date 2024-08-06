#Librería de selección aleatoria
from random import randint
while True:
         #Lista de opciones
         x = ["piedra", "papel", "tijera"]
         #Opcion de la maquina 
         computer = x[randint(0,2)]
         #Opcion del usuario
         player = input("piedra, papel o tijera? : ")
         #Logica del juego
         if player == computer:
               print("Empate")
         elif player == "piedra":
               if computer == "papel":
                print("Perdiste! ", computer, " > ", player)
               else:
                print("Ganaste !", player, " < ", computer)
         elif player == "papel":
                if computer == "tijera":
                            print("Perdiste! ", computer, " > ", player)
                else:
                            print("Ganaste! ", player, " < ", computer)
         elif player == "tijera":
                            if computer == "piedra":
                                   print("Perdiste! ", computer, " > ", player)
                            else:
                                    print("Ganaste! ", player, " < ", computer)
         else:
                 print("Error - Opción no valida, Intenta escribir las opciones como las vez.")