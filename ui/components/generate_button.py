from tkinter import Button


class GenerateButton():
    def __init__(self, root):
        self.root = root
        self.window = root.window

        self.button = Button(
            self.window,
            text="Generate",
            command=self.generate_command
        )
        self.button.pack()

        self.window.bind('<Return>', self.enter_command)

    def generate_command(self):
        """Button Click handler that generates a texture Json & generates an image"""
        self.root.texture_canvas.gen_image()


    def enter_command(self, event=None):
        self.generate_command()
