import tkinter as tk
from random import choice

class RPSGame:
    def __init__(self):
        self.window = (link unavailable)()
        self.window.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.player_history = []
        self.computer_history = []

        self.player_label = tk.Label(text="Player Score: 0")
        self.computer_label = tk.Label(text="Computer Score: 0")
        self.result_label = tk.Label(text="")

        self.rock_button = tk.Button(text="Rock", command=lambda: self.play("rock"))
        self.paper_button = tk.Button(text="Paper", command=lambda: self.play("paper"))
        self.scissors_button = tk.Button(text="Scissors", command=lambda: self.play("scissors"))

        self.player_label.pack()
        self.computer_label.pack()
        self.result_label.pack()
        self.rock_button.pack()
        self.paper_button.pack()
        self.scissors_button.pack()

    def play(self, player_choice):
        computer_choice = self.computer_move()
        self.player_history.append(player_choice)
        self.computer_history.append(computer_choice)

        if player_choice == computer_choice:
            self.result_label.config(text="It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            self.player_score += 1
            self.player_label.config(text=f"Player Score: {self.player_score}")
            self.result_label.config(text="You win!")
        else:
            self.computer_score += 1
            self.computer_label.config(text=f"Computer Score: {self.computer_score}")
            self.result_label.config(text="You lose!")

    def computer_move(self):
        if len(self.player_history) < 3:
            return choice(["rock", "paper", "scissors"])
        else:
            # Simple AI logic: choose the move that beats the player's most frequent move
            player_most_frequent = max(set(self.player_history), key=self.player_history.count)
            if player_most_frequent == "rock":
                return "paper"
            elif player_most_frequent == "paper":
                return "scissors"
            else:
                return "rock"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RPSGame()
    game.run()
