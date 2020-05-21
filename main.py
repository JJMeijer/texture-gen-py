from PIL import Image, ImageColor
from random import randint

texture_size = (20, 20) #pixels

texture = Image.new('L', (20,20))

palette = [
	{
		"hex": "#262A10",
		"prio": 60
	},
	{
		"hex": "#54442B",
		"prio": 20
	},
	{
		"hex": "#362417",
		"prio": 10
	},
	{
		"hex": "#141204",
		"prio": 10
	}
]


def gen_prio_list(palette):
	prio_list = []
	for index, color in enumerate(palette):
		prio_list += [index] * color['prio']
	
	return prio_list


def get_random_palette_color(palette, prio_list):
	random_index = prio_list[randint(0, len(prio_list))]

	return palette[random_index]['hex']


for row in range(texture_size[0]):
	for col in range(texture_size[1]):
		texture.putpixel((row, col), randint(0,255))

texture.show()

ImageColor.getrgb('#262A10')