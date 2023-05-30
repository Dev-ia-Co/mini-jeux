import random

class Mastermind:
    def __init__(self):
        self.code_length = 4  # Longueur du code
        self.num_colors = 6  # Nombre de couleurs disponibles
        self.max_attempts = 10  # Nombre maximum de tentatives
        self.colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Couleurs disponibles
    # Génère un code aléatoire
    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]
    # Obtient la supposition du joueur
    def get_guess(self):
        while True:
            guess = input("Enter your guess (4 colors from RGBYOP): ").upper()
            if len(guess) == self.code_length and all(color in self.colors for color in guess):
                return list(guess)
            else:
                print("Invalid guess. Please enter 4 colors from RGBYOP.")
    # Évalue la supposition du joueur et renvoie le nombre de correspondances exactes et de correspondances de couleur
    def evaluate_guess(self, code, guess):
        exact_matches = sum(1 for code_color, guess_color in zip(code, guess) if code_color == guess_color)
        color_matches = sum(min(code.count(color), guess.count(color)) for color in self.colors)
        return exact_matches, color_matches - exact_matches
    # Démarre le jeu Mastermind
    def play_game(self):
        print("Welcome to Mastermind!")
        code = self.generate_code()
        print("Code has been generated. Start guessing!")
        attempts = 0
        
        while attempts < self.max_attempts:
            guess = self.get_guess()
            attempts += 1
            exact_matches, color_matches = self.evaluate_guess(code, guess)
            
            print(f"Attempt {attempts}: {guess}")
            print(f"Exact Matches: {exact_matches}")
            print(f"Color Matches: {color_matches}")
            
            if exact_matches == self.code_length:
                print("Congratulations! You guessed the code correctly.")
                break
        
        if attempts == self.max_attempts:
            print(f"Game Over. You couldn't guess the code. The code was: {code}")

# Start the game
mastermind_game = Mastermind()
mastermind_game.play_game()
