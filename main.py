import app
import colors
from tkinter import *

# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)


class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Games in Tkinter")
        self.geometry("600x400")
        self.init_window()

    def init_window(self):
        menu = Menu(self)
        self.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        # Creating the SideBar as a child widget inside Window
        chat_app = app.GameApp(self)
        chat_app.pack(fill=BOTH, expand=True)

    def client_exit(self):
        exit()


if __name__ == "__main__":
    root = Window()
    # setting the minimum size of the root window
    root.minsize(600, 400)
    root.mainloop()