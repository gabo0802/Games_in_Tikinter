from tkinter import *
import random

class TicTacToe(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.board = [[" " for _ in range(3)] for _ in range(3)]  # Game board
        self.user = "X"  # User plays as "X"
        self.computer = "O"  # Computer plays as "O"

        self.create_widgets()

    def create_widgets(self):
        self.title_label = Label(self, text="Tic Tac Toe", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.board_frame = Frame(self)
        self.create_board()
        self.board_frame.grid(row=1, column=0, columnspan=3)


    def create_board(self):
            # Create the Tic Tac Toe board as a 3x3 grid of buttons
            for row in range(3):
                for col in range(3):
                    button = Button(self, text="", font=("Helvetica", 20), width=5, height=2,
                                    command=lambda r=row, c=col: self.make_move(r, c))
                    button.grid(row=row, column=col, padx=5, pady=5)



    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.user
            self.update_button(row, col)

            # Check if user wins
            if self.check_win(self.user):
                self.game_over_message("You win!")
                return

            # Check if the game is a draw
            if self.check_draw():
                self.game_over_message("It's a draw!")
                return

            # Computer's turn
            self.computer_move()

    def update_button(self, row, col):
        # Update the text of the button with the current player's symbol
        button = self.grid_slaves(row=row, column=col)[0]
        button.config(text=self.board[row][col], state=DISABLED)

    def computer_move(self):
        # Computer makes a random move
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == " "]
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = self.computer
            self.update_button(row, col)

            # Check if computer wins
            if self.check_win(self.computer):
                self.game_over_message("Computer wins!")
                return

            # Check if the game is a draw
            if self.check_draw():
                self.game_over_message("It's a draw!")
                return

    def check_win(self, player):
        # Check if a player has won
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        # Check if the game is a draw
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def game_over_message(self, message):
        # Display a game over message in a popup window
        top = Toplevel(self)
        for row in range(3):
            for col in range(3):
                button = self.grid_slaves(row=row, column=col)[0]
                button.config(state=DISABLED)

        top.title("Game Over")
        label = Label(top, text=message, font=("Helvetica", 20))
        label.pack(padx=10, pady=10)

# Test Function to test a counting game
def generate_count_frame(master):
    frame = Frame(master)
    count = 0

    def increment_count():
        nonlocal count
        count += 1
        label.config(text=f"Count: {count}")

    label = Label(frame, text="Count: 0")
    label.pack(padx=10, pady=10)

    button = Button(frame, text="Click to Count", command=increment_count)
    button.pack(padx=10, pady=10)

    return frame



