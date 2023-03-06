from tkinter import Tk

from .components import MenuBar
from .components import Title
from .components import GenerateButton
from .components import TextureCanvas
from .components import Setup


class Root:
    def __init__(self):
        window = Tk()
        window.geometry("1200x800")
        window.title("Texture Generator")

        self.window = window

        self.menubar = MenuBar(self)
        self.title = Title(self)
        self.generate_button = GenerateButton(self)
        self.texture_canvas = TextureCanvas(self)
        self.setup = Setup(self.window)

    def start(self):
        self.menubar.reset_command()
        self.window.mainloop()
