from tkinter import Label


class TitleLabel():
    def __init__(self, window):
        self.label = Label(
            window,
            text='Jumper Texture Generator',
            font=('Roboto', 35)
        )
        self.label.pack()
