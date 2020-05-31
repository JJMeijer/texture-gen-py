from tkinter import Canvas, LEFT
from PIL import Image, ImageTk
from generator.settings import texture_settings
from generator.texture import TextureGenerator

class TextureCanvas():
    def __init__(self, window):
        self.canvas = Canvas(window, width=500, height=500)
        self.canvas.pack(side=LEFT)

        self.img = ImageTk.PhotoImage('RGB')
        self.img_area = self.canvas.create_image(250, 250, image=self.img)
    

    def gen_image(self, settings):
        texture = TextureGenerator(settings).gen()
        texture = texture.resize((400, 400), Image.NEAREST)

        self.img = ImageTk.PhotoImage(texture)
        self.canvas.itemconfig(self.img_area, image=self.img)

