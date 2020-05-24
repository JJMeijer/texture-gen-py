from tkinter import Button


class GenButton():
    def __init__(self, window, command):
        self.button = Button(
            window,
            text="Generate",
            command=command
        )
        self.button.pack()