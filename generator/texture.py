from PIL import Image
from .core import TextureCoreGenerator
from .edge import TextureEdgeGenerator


class TextureGenerator:
    def __init__(self, settings):
        """Create a texture generator using a palette of colors and a size

        Args:
            settings (dict): Dictionary containing the settings for the to be generated texture
        """
        self.core = settings['core']
        self.edges = settings['edges']
        self.texture_size = settings['size']
        self.texture = Image.new('RGB', self.texture_size)

    def gen(self):
        edges = self.edges
        core_palette = self.core['palette']
        core_generator = TextureCoreGenerator(core_palette, self.texture)

        self.texture = core_generator.gen_core()

        if len(edges) > 0:
            for edge in edges:
                edge_generator = TextureEdgeGenerator(edge, self.texture)
                self.texture = edge_generator.gen_edge()

        return self.texture
