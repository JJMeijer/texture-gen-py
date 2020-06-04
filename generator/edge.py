from PIL import ImageColor
from random import randint

class TextureEdgeGenerator():
    def __init__(self, edge, texture):
        self.texture = texture
        self.edge_side = edge['side']
        self.width = edge['width']
        self.palette = edge['palette']

        self.gen_prio_list()
        self.set_edge()


    def set_edge(self):
        texture_size = self.texture.size
        edge_side = self.edge_side
        width = self.width

        if edge_side == 'top':
            self.edge = {
                'cols': list(range(texture_size[0])),
                'rows': list(range(0, width))
            }
        elif edge_side == 'bottom':
            self.edge = {
                'cols': list(range(texture_size[0])),
                'rows': list(range(texture_size[1] - width, texture_size[1]))
            }
        elif edge_side == 'left':
            self.edge = {
                'cols': list(range(0, width)),
                'rows': list(range(texture_size[1]))
            }
        elif edge_side == 'right':
            self.edge = {
                'cols': list(range(texture_size[0] - width, texture_size[0])),
                'rows': list(range(texture_size[1]))
            }


    def gen_prio_list(self):
        self.prio_list = []
        for index, color in enumerate(self.palette):
            self.prio_list += [index] * color['prio']


    def select_random_palette_color(self):
        color_index = self.prio_list[randint(0, len(self.prio_list)-1)]
        return self.palette[color_index]['hex']


    def gen_edge(self):
        edge = self.edge
        texture = self.texture

        for row in edge['rows']:
            for col in edge['cols']:
                random_color = self.select_random_palette_color()
                texture.putpixel((col, row), ImageColor.getrgb(random_color))

        return texture
