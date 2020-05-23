from generator.texture import TextureGenerator

texture_settings = {
	"size": (20,20),
	"core": {
		"palette": [
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
	},
	"edges": [
		{
			"side": "top",
			"width": 2,
			"palette": [
				{
					"hex": "#0b6623",
					"prio": 90
				},
				{
					"hex": "#109433",
					"prio": 10
				}
			]
		}
	]
}


generator = TextureGenerator(texture_settings)

random_texture = generator.gen()

random_texture.show()