import os
import random

class TicTacToe:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def create_board(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display_board(self):
        print(f"| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(f"| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(f"| {self.board[6]} | {self.board[7]} | {self.board[8]} |")

    def play_move(self, player, position):
        self.board[position] = player[0]

    def game_over(self):
        # Vérifier les lignes
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True

        # Vérifier les colonnes
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True

        # Vérifier les diagonales
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        # Vérifier s'il y a encore des mouvements possibles
        if " " not in self.board:
            return True

        return False

    def player_turn(self, player):
        os.system("clear")
        self.display_board()
        position = int(input(f"{player}, c'est à votre tour. Choisissez une position (1-9): ")) - 1
        while self.board[position] != " ":
            position = int(input("Position déjà occupée. Choisissez une autre position (1-9): ")) - 1
        self.play_move(player, position)

    def bot_turn(self, player, choice):
        os.system("clear")
        self.display_board()
        if choice == "1":
            position = self.random_IA()
        else:
            # TODO: Ajouter le code de l'IA ici
            pass
        print(f"L'IA a joué à la position {position + 1}")
        self.play_move(player, position)

    def random_IA(self):
        position = random.randint(0, 8)
        while self.board[position] != " ":
            position = random.randint(0, 8)
        return position

    def start_game(self):
        while True:
            self.create_board()
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
