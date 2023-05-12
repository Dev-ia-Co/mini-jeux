import random

class TicTacToe:
    # Initialisation du plateau
    def __init__(self) -> None:
        self.board = []
    # creation de la structure du Morpion
    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
    # Création d'un coup joué
    def play_pos(self, row, col, player):
        self.board[row][col] = player
    # Création du changement de tour
    def player_turn(self, player):
        return 'XO'[player == 'O']
    # affichage du plateau
    def show_board(self):
        print(*(' '.join(row) for row in self.board), sep='\n')
    # vérification victoire
    def is_player_win(self, player):
        n = len(self.board)
        win = any(
            all(self.board[i][j] == player for j in range(n))
            or all(self.board[j][i] == player for j in range(n))
            for i in range(n)
        )
        if all(self.board[i][i] == player for i in range(n)):
            return True
        if all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True
        return win
    # Vérification plateau complet
    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)
    def get_random_first_player(self):
        return random.randint(0,1)   
    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'

        while True:
            print(f"Player {player} turn")
            self.show_board()

            # prendre l'entrée de l'utilisateur
            row, col = list(map(int, input("Entrez les numéros de ligne et de colonne pour fixer l'emplacement : ").split()))
            print()

            # fixer l'emplacement
            self.fix_spot(row - 1, col - 1, player)

            # vérifier si le joueur actuel a gagné ou non
            if self.is_player_win(player):
                print(f"Le joueur {player} a gagné le jeu !")
                break

            # vérifier si le jeu est nul ou non
            if self.is_board_filled():
                print("Match nul !")
                break

            # changer le tour
            player = self.swap_player_turn(player)

        # afficher la vue finale de la grille
        print()
        self.show_board()