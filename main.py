from tkinter import *

class ChatApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.sidebar = Frame(self, width=150, relief=RAISED, background="#808080")
        self.sidebar.pack(side=LEFT, fill=Y)

        self.main_frame = Frame(self)
        self.main_frame.pack(side=LEFT, fill=BOTH, expand=True)

        self.frames = {}
        self.buttons = {}  # Dictionary to store buttons
        self.create_sidebar()
        self.create_frames()

    def create_sidebar(self):
        chats = ["Chat 1", "Chat 2", "Chat 3"]
        for i, chat in enumerate(chats):
            button = Button(self.sidebar, text=chat, command=lambda c=chat: self.show_frame(c), height=5, width=15, borderwidth=0)
            button.config(background="#808080", activebackground="#C0C0C0")
            button.pack(fill=Y, anchor="w")
            self.buttons[chat] = button

    def create_frames(self):
        for chat in ["Chat 1", "Chat 2", "Chat 3"]:
            frame = Frame(self.main_frame)
            Label(frame, text=chat).pack(padx=10, pady=10)
            self.frames[chat] = frame

        # Show the first chat frame by default
        self.current_frame = None
        self.show_frame("Chat 1")

    def show_frame(self, chat):
        frame = self.frames[chat]
        if self.current_frame:
            self.current_frame.pack_forget()
        frame.pack(fill=BOTH, expand=True)
        self.current_frame = frame

        # Update the selected chat and highlight the corresponding button
        for chat_name, button in self.buttons.items():
            if chat_name == chat:
                button.config(background="#C0C0C0")
            else:
                button.config(background="#808080")


class Window(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GUI")
        self.geometry("400x300")
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

        # Creating the ChatApp as a child widget inside Window
        chat_app = ChatApp(self)
        chat_app.pack(fill=BOTH, expand=True)

    def client_exit(self):
        exit()


if __name__ == "__main__":
    root = Window()

    # setting the minimum size of the root window
    root.minsize(600, 400)

    root.mainloop()    