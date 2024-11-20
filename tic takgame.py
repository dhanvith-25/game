import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"  # X starts the game
        self.board = [None] * 9  # Board is a list of 9 cells
        self.buttons = []  # List to store the button widgets
        
        # Create the buttons for the Tic-Tac-Toe grid
        for i in range(9):
            button = tk.Button(self.root, text="", font="Arial 20", width=5, height=2, 
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, i):
        if self.board[i] is None:  # Only allow move if the cell is empty
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        """Switch between player X and O"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if there is a winner"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False

    def reset_game(self):
        """Reset the game board for a new game"""
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"


# Create the main window
root = tk.Tk()

# Create an instance of the TicTacToe game
game = TicTacToe(root)

# Run the Tkinter event loop
root.mainloop()
