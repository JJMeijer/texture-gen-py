from tkinter import Tk, Label, Button, Canvas
from .canvas import TextureCanvas

window = Tk()

window.geometry('800x640')
window.title("Jumper Texture Generator")

lbl_title = Label(
    window,
    text='Texture Generator',
    font=('Roboto', 45)
)
lbl_title.pack()


def on_gen_button():
    texture_image.gen_image()


gen_button = Button(
    window,
    text="Generate",
    command=on_gen_button
)
gen_button.pack()

texture_image = TextureCanvas(window)

window.mainloop()