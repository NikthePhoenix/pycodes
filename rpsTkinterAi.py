import tkinter as tk
from random import choice
import sqlite3

class RPSGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0
        self.player_history = []
        self.computer_history = []

        # Connect to the database
        self.conn = sqlite3.connect("rps.db")
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                player_choice TEXT,
                computer_choice TEXT,
                result TEXT
            )
        """)

        # Load the player's history and scores from the database
        self.load_history()

        # GUI elements
        self.player_label = tk.Label(text=f"Player Score: {self.player_score}")
        self.computer_label = tk.Label(text=f"Computer Score: {self.computer_score}")
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

        # Save the game to the database
        self.cursor.execute("""
            INSERT INTO games (player_choice, computer_choice, result)
            VALUES (?, ?, ?)
        """, (player_choice, computer_choice, self.determine_result(player_choice, computer_choice)))
        self.conn.commit()

        # Update the scores and labels
        self.update_scores()
        self.player_label.config(text=f"Player Score: {self.player_score}")
        self.computer_label.config(text=f"Computer Score: {self.computer_score}")
        self.result_label.config(text=self.determine_result(player_choice, computer_choice))

    def computer_move(self):
        # Simple AI logic: choose the move that beats the player's most frequent move
        player_most_frequent = max(set(self.player_history), key=self.player_history.count)
        if player_most_frequent == "rock":
            return "paper"
        elif player_most_frequent == "paper":
            return "scissors"
        else:
            return "rock"

    def determine_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
            self.player_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def load_history(self):
        self.cursor.execute("SELECT player_choice, computer_choice FROM games")
        rows = self.cursor.fetchall()
        for row in rows:
            self.player_history.append(row[0])
            self.computer_history.append(row[1])

    def update_scores(self):
        self.cursor.execute("SELECT COUNT(*) AS count FROM games WHERE result = 'You win!'")
        self.player_score = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) AS count FROM games WHERE result = 'You lose!'")
        self.computer_score = self.cursor.fetchone()[0]

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RPSGame()
    game.run()
