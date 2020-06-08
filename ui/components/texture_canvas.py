from tkinter import Canvas, Frame, CENTER
from PIL import Image, ImageTk
from generator.texture import TextureGenerator

class TextureCanvas():
    def __init__(self, root):
        self.root = root
        self.window = root.window

        self.texture_frame = Frame(self.window)
        self.texture_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.canvas = Canvas(self.texture_frame, width=500, height=500)
        self.canvas.pack()

        self.img = ImageTk.PhotoImage('RGB')
        self.img_area = self.canvas.create_image(250, 250, image=self.img)


    def gen_image(self):
        """Generate an image using the TextureGenerator class and a settings Dictionary

        :param settings: Settings dictionary which is used as input for the Generator
        :type settings: dict
        """
        setup_obj = self.root.setup.parse_setup()

        texture = TextureGenerator(setup_obj).gen()
        texture = texture.resize((400, 400), Image.NEAREST)

        self.img = ImageTk.PhotoImage(texture)
        self.canvas.itemconfig(self.img_area, image=self.img)