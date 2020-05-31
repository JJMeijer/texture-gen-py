from tkinter import Tk, Label, Button
from .texture import TextureCanvas
from .labels import TitleLabel
from .buttons import GenButton
from .settings import Settings

window = Tk()

window.geometry('1200x800')
window.title("Jumper Texture Generator")

def handle_color_input(color):
    c_hex = color['hex'].get()
    c_prio= int(color['prio'].get())

    return {
        'hex': c_hex,
        'prio': c_prio
    }


def handle_edge_input(edge):
    return {
        'side': edge['side'].get(),
        'width': int(edge['width'].get()),
        'palette': list(map(handle_color_input, edge['colors']))
    }


def generate_texture_settings():
    size = (
        int(settings.size_settings.width.get()),
        int(settings.size_settings.height.get()),
    )

    core_palette = list(map(handle_color_input, settings.core_settings.colors))
    edges = list(map(handle_edge_input, settings.edge_settings.edges))
    
    return {
        "size": size,
        "core": {
            "palette": core_palette
        },
        "edges": edges
    }

def on_gen_button():
    settings = generate_texture_settings()
    texture_image.gen_image(settings)


title_label = TitleLabel(window)
gen_button = GenButton(window, on_gen_button)
texture_image = TextureCanvas(window)
settings = Settings(window)

window.mainloop()