import tkinter as tk
from tkinter import messagebox
from queue import Queue

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 24), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.turn_label = tk.Label(self.root, text="Player X's Turn", font=("Helvetica", 14))
        self.turn_label.grid(row=3, columnspan=3)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.result_label.config(text=f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                self.result_label.config(text="It's a tie!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        move = self.bfs()
        if move:
            row, col = move
            self.make_move(row, col)

    def bfs(self):
        queue = Queue()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    queue.put((i, j))

        while not queue.empty():
            row, col = queue.get()
            self.board[row][col] = "O"
            if self.check_winner():
                self.board[row][col] = ""
                return row, col
            self.board[row][col] = ""

        return None

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="", state="normal")
        self.current_player = "X"
        self.turn_label.config(text="Player X's Turn")
        self.result_label.config(text="")


if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
