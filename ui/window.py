from tkinter import Tk, Label, Button
from .texture import TextureCanvas
from .labels import TitleLabel
from .buttons import GenButton

window = Tk()

window.geometry('800x640')
window.title("Jumper Texture Generator")


def on_gen_button():
    texture_image.gen_image()


title_label = TitleLabel(window)
gen_button = GenButton(window, on_gen_button)
texture_image = TextureCanvas(window)

window.mainloop()