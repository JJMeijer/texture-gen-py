import json
from tkinter import Frame
from tkinter import RIGHT, END
from tkinter.filedialog import asksaveasfile, askopenfile

from .core_setup import CoreSetup
from .size_setup import SizeSetup
from .edge_setup import EdgeSetup


class Setup:
    def __init__(self, parent):
        self.parent = parent

        self.settings_frame = Frame(parent)
        self.settings_frame.pack(side=RIGHT)

        self.size_setup = SizeSetup(self.settings_frame)
        self.core_setup = CoreSetup(self.settings_frame)
        self.edge_setup = EdgeSetup(self.settings_frame)

    def handle_color_input(self, color):
        c_hex = color["hex"].get()
        c_prio = int(color["prio"].get())

        return {"hex": c_hex, "prio": c_prio}

    def handle_edge_input(self, edge):
        return {
            "side": edge["side"].get(),
            "width": int(edge["width"].get()),
            "palette": list(map(self.handle_color_input, edge["palette"])),
        }

    def parse_setup(self):
        size = (
            int(self.size_setup.width.get()),
            int(self.size_setup.height.get()),
        )

        core_palette = list(map(self.handle_color_input, self.core_setup.palette))
        edges = list(map(self.handle_edge_input, self.edge_setup.edge_data))

        return {"size": size, "core": {"palette": core_palette}, "edges": edges}

    def process_import(self, setup_dict):
        size = setup_dict["size"]
        width_field = self.size_setup.width
        height_field = self.size_setup.height

        width_field.delete(0, END)
        width_field.insert(0, size[0])

        height_field.delete(0, END)
        height_field.insert(0, size[1])

        core = setup_dict["core"]
        core_palette = core["palette"]

        self.core_setup.flush_colors()

        for color in core_palette:
            self.core_setup.add_color_field(color=color)

        edges = setup_dict["edges"]

        self.edge_setup.flush_edges()

        for edge in edges:
            side = edge["side"]
            width = edge["width"]
            palette = edge["palette"]
            self.edge_setup.add_edge(side, width, palette)

    def process_save_setup(self):
        data = self.parse_setup()
        data_string = json.dumps(data, indent=4)

        file = asksaveasfile(
            mode="w",
            title="Save Setup",
            filetypes=(("JSON", "*.json"),),
            defaultextension="",
        )

        if file:
            file.write(data_string)
            file.close()

    def process_load_setup(self):
        file = askopenfile(mode="r", title="Load Setup", filetypes=(("JSON", "*json"),))

        if file:
            data_string = file.read()
            data = json.loads(data_string)
            self.process_import(data)
