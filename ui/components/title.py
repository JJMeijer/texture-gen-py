from tkinter import Label


class Title():
    def __init__(self, root):
        self.window = root.window

        self.label = Label(
            self.window,
            text='Jumper Texture Generator',
            font=('Roboto', 35)
        )
        self.label.pack()
