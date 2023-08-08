from tkinter import *
from colors import *  # Import colors from the colors.py file
from games import *

class GameApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Sidebar to hold game selection buttons
        self.sidebar = Frame(self, width=150, relief=RAISED, background=blue_1)
        self.sidebar.pack(side=LEFT, fill=Y)

        # Main frame to display the selected game's content
        self.main_frame = Frame(self)
        self.main_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.frames = {}   # Dictionary to store frames of different games
        self.buttons = {}  # Dictionary to store buttons of different games
        self.create_sidebar()
        self.create_frames()

    def create_sidebar(self):
        # Games available for selection
        games = ["Tic Tac Toe", "Wordle", "Anagrams"]
        for i, game in enumerate(games):
            button = Button(self.sidebar, text=game, command=lambda c=game: self.show_frame(c), height=5, width=15, borderwidth=0)
            button.config(background=blue_1, activebackground=blue_2)
            button.pack(fill=Y, anchor="w")
            self.buttons[game] = button

    def create_frames(self):
        # Create frames for each game and store them in the frames dictionary
        for game in ["Tic Tac Toe", "Wordle", "Anagrams"]:
            frame = Frame(self.main_frame, background=orange_0)
            Label(frame, text=game).pack(padx=10, pady=10)
            self.frames[game] = frame

        # Show the first game frame (Tic Tac Toe) by default
        self.current_frame = None
        self.show_frame("Tic Tac Toe")

    def create_frames(self):
        # Create frames for each game and store them in the frames dictionary
        for game in ["Tic Tac Toe", "Wordle", "Anagrams"]:
            frame = Frame(self.main_frame, background=orange_0)
            self.frames[game] = frame

        # Initialize a TicTacToe object for the "Tic Tac Toe" game
        self.tic_tac_toe = TicTacToe(self.frames["Tic Tac Toe"])
        self.tic_tac_toe.create_board()

        # Show the first game frame (Tic Tac Toe) by default
        self.current_frame = None
        self.show_frame("Tic Tac Toe")

    def show_frame(self, game):
        frame = self.frames[game]
        if self.current_frame:
            self.current_frame.pack_forget()

        frame.pack(fill=BOTH, expand=True)
        self.current_frame = frame

        if game == "Tic Tac Toe":
            self.tic_tac_toe.pack_forget()  # Remove the old TicTacToe board
            self.tic_tac_toe = TicTacToe(frame)  # Create a new TicTacToe object
            self.tic_tac_toe.create_board()  # Create the new board
            self.tic_tac_toe.pack()  # Pack the new board
        else:
            # Add logic for other games here
            pass

        for game_name, button in self.buttons.items():
            if game_name == game:
                button.config(background=blue_2)
            else:
                button.config(background=blue_1)
