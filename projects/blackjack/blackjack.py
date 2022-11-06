# Declaración de módulos
from art import logo
import random
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def choose_card(): # Función de seleccion de cartas aleatorias
    return random.choice(cards)

def calculation_score():
    if sum(user_cards) == 21 and len(user_cards) == 2:
        return 21
    if 11 in user_cards and sum(user_cards) > 21:
        user_cards.remove(11)
        user_cards.append(1)
    return sum(user_cards)
    
def current_result(): # Función de mostrar resultado actual de la partida
    user_result = print(f'Your cards: {user_cards} Current score: {total_user_card}')
    cpu_result = print(f'Computer\'s card: {cpu_cards} Current score: {total_cpu_card}')
    return user_result, cpu_result

def lose_game(): # Función que indica perdida de juego
    print('You went over. You lose 😓')
    play_game = False

def win_game(): # Función que indica perdida de juego
    print('Opponent went over. You win 😁')
    play_game = False

play_game = True # Bandera de continuidad del juego

while play_game:
    
    user_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") # Input usuario
    
    if user_answer == 'y':

        clear()
        
        print(logo) # Llamar logo ASCII

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Declaración de cartas

        # Arreglos vacíos donde se agregará cada maso
        user_cards = [] 
        cpu_cards = []

        # Insercción de primeras cartas para el usuario y cpu
        for i in range(2):
            user_cards.append(choose_card())

        # Insercción de primeras cartas para el cpu    
        cpu_cards.append(choose_card())
        
        # Suma de totales actuales para usuario y cpu con cartas actuales
        total_user_card = calculation_score()
        total_cpu_card = sum(cpu_cards)

        # Impresión de resultados actuales
        current_result()

        adding_cards = True # Bandera de inicio agregar cartas

        while adding_cards:

            add_card = input("Type 'y' to get another card, type 'n' to pass: ") # Input del usuario
            
            if add_card == 'y': # En caso de seleccionar 'y'
                user_cards.append(choose_card()) # Agregar una nueva carta
                total_user_card = sum(user_cards) # Sumar el total de cartas actual
                current_result() # Mostrar el resultado actual
                if total_user_card > 21: # Si agregada la carta es mayor a 21
                    lose_game() # Indicar perdida de juego
                    adding_cards = False # Salir del loop de agregar cartas
            
            else: # En caso de seleccionar 'n'
                while total_cpu_card < total_user_card: # Inicio de loop de agregar las cartas cpu si es menor al valor del usuario
                    cpu_cards.append(choose_card()) # Agregar carta a cpu
                    total_cpu_card = sum(cpu_cards) # Sumar total de cartas a cpu
                    if total_cpu_card > total_user_card and total_cpu_card <= 21:
                        current_result()
                        lose_game()
                        adding_cards = False
                    elif total_cpu_card > 21:
                        current_result()
                        win_game()
                        adding_cards = False
                            
    else:
        play_game = False
      
