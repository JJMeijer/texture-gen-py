from generator import TextureGenerator

palette = [
	{
		"hex": "#2b1d12",
		"prio": 20
	},
	{
		"hex": "#855838",
		"prio": 10
	},
	{
		"hex": "#362417",
		"prio": 80
	},
	{
		"hex": "#33251a",
		"prio": 10
	}
]

generator = TextureGenerator(palette, 10)

random_texture = generator.gen()

random_texture.show()