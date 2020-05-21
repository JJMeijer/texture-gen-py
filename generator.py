from PIL import Image, ImageColor
from random import randint

def gen_prio_list(palette):
	prio_list = []
	for index, color in enumerate(palette):
		prio_list += [index] * color['prio']
	
	return prio_list


class TextureGenerator:
	def __init__(self, palette, size):
		"""Create a texture generator using a palette of colors and a size

		Args:
			palette (list): a List of dictionaries.	each dictionary has a hex color value and a prio value which describes a relative importance of that color in the texture
			texture_size (int): size of the texture. (x, y) size of the texture will take this value
		"""		
		self.palette = palette
		self.texture_size = (size, size)
		self.prio_list = gen_prio_list(self.palette)
		self.texture = Image.new('RGB', self.texture_size)


	def get_palette_color(self, index):
		"""Get the hex value of a pallete item given an index

		Args:
			index (int): index integer of the color that needs to be returned

		Returns:
			str: string Hex color value that is found at the palette index
		"""		
		return self.palette[index]['hex']


	def select_random_palette_color(self):
		"""Generate a random palette index given the prio's defined in the palette list

		Returns:
			int: random index integer that corresponds to an item in the palette list
		"""		
		prio_list = self.prio_list
		return prio_list[randint(0, len(prio_list)-1)]


	def gen(self):
		texture_size = self.texture_size
		texture = self.texture

		for row in range(texture_size[0]):
			for col in range(texture_size[1]):
				random_color_index = self.select_random_palette_color()
				random_color = self.get_palette_color(index=random_color_index)
				texture.putpixel((row, col), ImageColor.getrgb(random_color))
		
		return texture