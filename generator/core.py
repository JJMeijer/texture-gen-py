from random import randint
from PIL import ImageColor


class TextureCoreGenerator:
    def __init__(self, palette, texture):
        """Generator class for a texture Core

        Args:
            palette (list): list of Dictionaries containing a hex color value and a prio value.
            texture (Image): Pillow Image class.
        """
        self.texture = texture
        self.palette = palette
        self.gen_prio_list()


    def gen_prio_list(self):
        """Generate a list which gives a representation of priority of each
        index within a palette list

        Args:
            palette (list): list of Dictionaries containing a hex color value and a prio value.

        Returns:
            list: list containing the palette priority representation
        """
        self.prio_list = []
        for index, color in enumerate(self.palette):
            self.prio_list += [index] * color['prio']


    def select_random_palette_color(self):
        """Select Random color from the palette List

        :return: Random color Dictionary from the palette List
        :rtype: dict
        """
        color_index = self.prio_list[randint(0, len(self.prio_list)-1)]
        return self.palette[color_index]['hex']


    def gen_core(self):
        """Loop through texture and give each pixel in the texture a random color.
        The random color is picked from the prio_list.

        Returns:
            Image: Pillow Image class containing the texture
        """
        texture = self.texture

        for row in range(texture.size[0]):
            for col in range(texture.size[1]):
                random_color = self.select_random_palette_color()

                texture.putpixel((col, row), ImageColor.getrgb(random_color))

        return texture
