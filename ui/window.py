import re

from tkinter import Tk
from tkinter import END

from .texture import TextureCanvas
from .labels import TitleLabel
from .buttons import GenButton
from .settings import Settings
from .settings.default_settings import DefaultSettings
from .menubar import MenuBar


window = Tk()

window.geometry('1200x800')
window.title("Jumper Texture Generator")



def delete_colors_from_core(core_color_group):
    children = core_color_group.children
    delete_list = []
    for child in children:
        if re.search('frame', child):
            children[child].pack_forget()
            delete_list.append(children[child])

    while len(delete_list) > 0:
        child = delete_list.pop()
        child.destroy()


def delete_edges_from_group(edge_group):
    children = edge_group.children
    delete_list = []
    for child in children:
        if re.search('labelframe', child):
            children[child].pack_forget()
            delete_list.append(children[child])

    while len(delete_list) > 0:
        child = delete_list.pop()
        child.destroy()


def process_settings_import(settings_dict):
    size = settings_dict['size']
    width_field = tk_settings.size_settings.width
    height_field = tk_settings.size_settings.height

    width_field.delete(0, END)
    width_field.insert(0, size[0])

    height_field.delete(0, END)
    height_field.insert(0, size[1])

    core = settings_dict['core']
    core_palette = core['palette']

    core_color_group = tk_settings.core_settings.color_group
    tk_settings.core_settings.colors = [] # Reset colors list, not fun :(
    delete_colors_from_core(core_color_group)

    for color in core_palette:
        tk_settings.core_settings.add_color_field(
            color=color
        )


    edges = settings_dict['edges']
    edge_group = tk_settings.edge_settings.edge_group
    tk_settings.edge_settings.edges = [] # Reset Edges list, also not fun :(
    delete_edges_from_group(edge_group)

    for edge in edges:
        side = edge['side']
        width = edge['width']
        palette = edge['palette']
        tk_settings.edge_settings.add_edge_frame(side, width, palette)


def handle_color_input(color):
    """Color Input handler

    :param color: Tkinter Entry class for a color field.
    :type color: class
    :return: Dictionary containing a hex color string and a prio value
    :rtype: dict
    """
    c_hex = color['hex'].get()
    c_prio = int(color['prio'].get())

    return {
        'hex': c_hex,
        'prio': c_prio
    }


def handle_edge_input(edge):
    """Function that handles the Entries for an edge when the generate button is clicked.

    :param edge: Dictionary containing the Entry fields of an edge
    :type edge: dict
    :return: dict
    :rtype: Parsed input values from the Entry fields of an edge
    """
    return {
        'side': edge['side'].get(),
        'width': int(edge['width'].get()),
        'palette': list(map(handle_color_input, edge['palette']))
    }


def generate_texture_settings():
    """Generate Texture JSON by parsing the Entries in the TkInter settings object.

    :param tk_settings: Dictionary containing the TKinter entries in the settings object
    :type tk_settings: dict
    :return: Dictionary containing the parsed values
    :rtype: dict
    """
    size = (
        int(tk_settings.size_settings.width.get()),
        int(tk_settings.size_settings.height.get()),
    )

    core_palette = list(map(handle_color_input, tk_settings.core_settings.colors))
    edges = list(map(handle_edge_input, tk_settings.edge_settings.edges))

    return {
        "size": size,
        "core": {
            "palette": core_palette
        },
        "edges": edges
    }

def on_gen_button():
    """Button Click handler that generates a texture Json & generates an image"""
    texture_settings = generate_texture_settings()
    texture_image.gen_image(texture_settings)


def reset_command():
    process_settings_import(DefaultSettings)
    texture_settings = generate_texture_settings()
    texture_image.gen_image(texture_settings)


menubar = MenuBar(window, reset_command)
title_label = TitleLabel(window)
gen_button = GenButton(window, on_gen_button)
texture_image = TextureCanvas(window)
tk_settings = Settings(window)

reset_command() # Reset to default settings on start
window.mainloop()
