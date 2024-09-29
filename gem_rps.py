import tkinter as tk
import random

# Game states
ROCK = 0
PAPER = 1
SCISSORS = 2

# Game outcomes
WIN = 1
LOSE = -1
DRAW = 0

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors")

        # Labels to display the score
        self.player_score_label = tk.Label(self.root, text="Player Score: 0")
        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0")
        self.player_score_label.pack()
        self.computer_score_label.pack()

        # Buttons for player choices
        self.rock_button = tk.Button(self.root, text="Rock", command=self.play_rock)
        self.paper_button = tk.Button(self.root, text="Paper", command=self.play_paper)
        self.scissors_button = tk.Button(self.root, text="Scissors", command=self.play_scissors)
        self.rock_button.pack()
        self.paper_button.pack()
        self.scissors_button.pack()

        # Label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        # Button to end the game
        self.end_game_button = tk.Button(self.root, text="End Game", command=self.root.quit)
        self.end_game_button.pack()

        # Initialize scores
        self.player_score = 0
        self.computer_score = 0

    def play_rock(self):
        self.play_round(ROCK)

    def play_paper(self):
        self.play_round(PAPER)

    def play_scissors(self):
        self.play_round(SCISSORS)

    def play_round(self, player_choice):
        computer_choice = random.randint(0, 2)

        if player_choice == computer_choice:
            result = DRAW
            result_text = "It's a tie!"
        elif (player_choice == ROCK and computer_choice == SCISSORS) or \
            (player_choice == PAPER and computer_choice == ROCK) or \
            (player_choice == SCISSORS and computer_choice == PAPER):
            result = WIN
            result_text = "You win!"
            self.player_score += 1
        else:
            result = LOSE
            result_text = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=result_text)
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()