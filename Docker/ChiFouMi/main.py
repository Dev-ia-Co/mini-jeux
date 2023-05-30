import os
import random

class Chifoumi:
    def __init__(self):
        self.choices = ["pierre", "feuille", "ciseaux"]
    
    # Obtient le choix de l'utilisateur et le valide.
    def get_user_choice(self):
        while True:
            choice = input("Choisissez pierre, feuille ou ciseaux: ").lower()
            if choice in self.choices:
                return choice
            else:
                print("Choix invalide. Veuillez réessayer.")
    # Génère aléatoirement le choix de l'ordinateur.
    def get_computer_choice(self):
        return random.choice(self.choices)
    # Détermine le gagnant en comparant les choix de l'utilisateur et de l'ordinateur.
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "match nul"
        elif (user_choice == "pierre" and computer_choice == "ciseaux") or (user_choice == "feuille" and computer_choice == "pierre") or (user_choice == "ciseaux" and computer_choice == "feuille"):
            return "Vous avez gagné !"
        else:
            return "L'ordinateur a gagné !"
    # Lance le jeu Chifoumi.
    def play_game(self):
        print("Bienvenue dans le jeu de Chifoumi !")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"Vous avez choisi : {user_choice}")
            print(f"L'ordinateur a choisi : {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            play_again = input("Voulez-vous rejouer ? (o/n) : ").lower()
            if play_again != "o":
                break

# Démarrer le jeu
chifoumi_game = Chifoumi()
chifoumi_game.play_game()
