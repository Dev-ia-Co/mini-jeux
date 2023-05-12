import os

# Créer la grille du tic-tac-toe
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Fonction pour afficher la grille
def display_board():
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

# Fonction pour jouer un coup
def play_move(player, position):
    board[position] = player

# Fonction pour vérifier si le jeu est terminé
def game_over():
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
def player_turn(player):
    os.system("clear")
    display_board()
    position = int(input(f"{player}, c'est à votre tour. Choisissez une position (1-9): ")) - 1
    while board[position] != " ":
        position = int(input("Position déjà occupée. Choisissez une autre position (1-9): ")) - 1
    play_move(player, position)

# Fonction pour démarrer le jeu
def start_game():
    player1 = input("Joueur 1, entrez votre nom: ")
    player2 = input("Joueur 2, entrez votre nom: ")
    while not game_over():
        player_turn("X")
        if game_over():
            break
        player_turn("O")
    os.system("clear")
    display_board()
    if " " not in board:
        print("Match nul !")
    else:
        winner = "Joueur 1" if board.count("X") > board.count("O") else "Joueur 2"
        print(f"{winner} a gagné !")

# Démarrer le jeu
start_game()
