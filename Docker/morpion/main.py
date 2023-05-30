import os
import random
# Créer la grille du tic-tac-toe
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def create_board():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Fonction pour afficher la grille
def display_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

# Fonction pour jouer un coup
def play_move(board, player, position):
    board[position] = player[0]

# Fonction pour vérifier si le jeu est terminé
def game_over(board):
    # Vérifier les lignes
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    
    # Vérifier les colonnes
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    
    # Vérifier les diagonales
    if board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    
    # Vérifier s'il y a encore des mouvements possibles
    if " " not in board:
        return True
    
    return False

# Fonction pour le tour d'un joueur
def player_turn(board, player):
    os.system("clear")
    display_board(board)
    position = int(input(f"{player}, c'est à votre tour. Choisissez une position (1-9): ")) - 1
    while board[position] != " ":
        position = int(input("Position déjà occupée. Choisissez une autre position (1-9): ")) - 1
    play_move(board, player, position)

# Fonction pour le tour d'une IA
def bot_turn(board, player, choice):
    os.system("clear")
    display_board(board)
    if choice == "1":
        position = random_IA(board)
    else:
        # TODO: Ajouter le code de l'IA ici
        pass
    print(f"L'IA a joué à la position {position + 1}")
    play_move(board, player, position)

def random_IA(board):
    position = random.randint(0, 8)
    while board[position] != " ":
            position = random.randint(0, 8)
    return position

# Fonction pour démarrer le jeu
def start_game():
    while True:
     global board
     board = create_board()
     choice = input("Choisissez un adversaire :  contre un humain (1) ou une IA (2) ou IA contre IA (3)? ")
     if choice == "1":
        player1 = "X"
        player2 = "O"
        break
     elif choice == "2":
        player1 = "X"
        player2 = "O (IA)"
        break
     elif choice == "3":
        player1 = "X (IA1)"
        player2 = "O (IA2)"
        break
     else:
        print("Choix invalide, veuillez choisir 1, 2 ou 3")

    while not game_over(board):
        if player1.endswith("(IA1)"):
            bot_turn(board, player1, "1") # random test
        else:
            player_turn(board, player1)
        if game_over(board):
            break
        if player2 == "O":
            player_turn(board, player2)
        elif player2 == "O (IA)":
            bot_turn(board, player2, "1")
        elif player2 == "O (IA2)":
            bot_turn(board, player2, "1")
    os.system("clear")
    display_board(board)

    while True:
        choice = input("Voulez-vous rejouer ? (O/N) : ")
        if choice.upper() == "O":
            start_game()
            break
        elif choice.upper() == "N":
            print("Merci d'avoir joué !")
            break
        else:
            print("Choix invalide, veuillez choisir O ou N.")

# Démarrer le jeu
start_game()
