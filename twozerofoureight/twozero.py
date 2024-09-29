import tkinter as tk
import random

class GameBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.grid_size = 4
        self.board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0
        self.game_over = False

        # ... (create UI elements)

        self.bind_keys()
        self.generate_new_tile()
        self.update_board()

    def bind_keys(self):
        self.master.bind("<Left>", lambda event: self.move_tiles("left"))
        self.master.bind("<Right>", lambda event: self.move_tiles("right"))
        self.master.bind("<Up>", lambda event: self.move_tiles("up"))
        self.master.bind("<Down>", lambda event: self.move_tiles("down"))

    def move_tiles(self, direction):
        if self.game_over:
            return

        moved = False
        merged = False

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                tile = self.board[row][col]
                if tile == 0:
                    continue

                new_row, new_col = row, col
                if direction == "left":
                    new_col = max(0, col - 1)
                elif direction == "right":
                    new_col = min(self.grid_size - 1, col + 1)
                elif direction == "up":
                    new_row = max(0, row - 1)
                elif direction == "down":
                    new_row = min(self.grid_size - 1, row + 1)

                if self.board[new_row][new_col] == 0:
                    self.board[new_row][new_col] = tile
                    self.board[row][col] = 0
                    moved = True
                elif self.board[new_row][new_col] == tile:
                    self.board[new_row][new_col] *= 2
                    self.board[row][col] = 0
                    self.score += self.board[new_row][new_col]
                    moved = True
                    merged = True

        if moved:
            self.generate_new_tile()
            self.update_board()
            self.check_game_over()

    def generate_new_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 2 if random.random() < 0.9 else 4

    # def update_board(self):
    #     # ... (update board UI)

    def check_game_over(self):
        if not any(0 in row for row in self.board) and all(self.board[i][j] != self.board[i + 1][j] and self.board[i][j] != self.board[i][j + 1] for i in range(self.grid_size - 1) for j in range(self.grid_size - 1)):
            self.game_over = True
            # ... (handle game over)

if __name__ == "__main__":
    root = tk.Tk()
    game = GameBoard(root)
    root.mainloop()